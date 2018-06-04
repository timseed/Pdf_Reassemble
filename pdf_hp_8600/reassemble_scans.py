from glob import glob
import PyPDF2
import daiquiri


class reassemble_scans(object):
    """
    Class to reassemble a multipage scan document
    Useage:
    rs = reassemble_scans("Directory_where_2_pdfs_live")
    rs.find_finds()
    rs.reassemble("/tmp/new_document.pdf")
    """

    def __init__(self,directory_for_scans):
        self.dir_to_search=directory_for_scans
        self.logging = daiquiri.getLogger(__name__)


    def help(self):
        message=\
"""
The 8600 Pro scanner, does not allow you to do double sided scanning. Which is a shame as its double sided printing is excellent.

Instead what you need to do is as follows.

Get the Pages nicely stacked together and place them on the top of the scanner. 
Put a USB Drive (Win32 or maybe ntfs) into the printer
Put the Documents on the top of the scanner - in the scanner feeder
Using the front screen, Right Arrow - Select Scan - then select the Green Button Scan.
When all the documents are done....
Rotate the documents 180 degrees and put them back in the scanner. Do not turn them head over heels - just rotatoe them 180 Degrees
Press Scan for the 2nd time.

At the end of this (wait for the scan to finish) - and then pull out the USB drive.

You should find 2 pdf documents

The first will have pages (1,3,5,7,9) on it.... then 2nd will have pages (10,8,6,4,2)

This script will make the new_document have pages in the order of (1,2,3,4,....)

"""
        print(""+message)
        return message


    def find_finds(self,dir=None):
        """

        :param dir:
        :return: Length of the number of files found in the directory
        """
        if dir==None:
            where=self.dir_to_search
        else:
            where=dir
        self.files = glob(where+"/*.pdf")

        for f in self.files:
            print("{}".format(f))
            self.logging.info("Files are {}".format(f))
        return len(self.files)

    def check_2_scans(self):
        """
        There should only be 2 pdf documents in the target directory
        :return:
        """
        if len(self.files) == 2:
            self.logging.debug("Correct number of files found")
            return True

    def reassemble(self,new_file_name):
        """
        reassemble the 2 scans into a new document
        :param new_file_name: Name of the new document  - should have pdf as a suffix
        :return:  True if Ok - ValueError if the {ageCount is different

        """
        try:

            f1 = PyPDF2.PdfFileReader(open(self.files[0], 'rb'))
            f2 = PyPDF2.PdfFileReader(open(self.files[1], 'rb'))

            self.logging.debug("F1 Has {} Pages".format(f1.getNumPages()))
            self.logging.debug("F2 Has {} Pages".format(f2.getNumPages()))

            if f1.getNumPages() == f2.getNumPages():
                f2_next_page = f2.getNumPages() - 1
                f1_next_page = 1

                new_doc = PyPDF2.PdfFileWriter()
                while f1_next_page < f1.getNumPages():
                    new_doc.addPage(f1.getPage(f1_next_page))
                    new_doc.addPage(f2.getPage(f2_next_page))
                    self.logging.info("Page {} and {} added ".format(f1_next_page, f2_next_page))
                    f1_next_page += 1
                    f2_next_page -= 1
                new_doc.write(open(new_file_name, "wb"))
                return True
            else:
                return False
        except Exception as err:
            self.logging("Error {} ".format(str(err)))
            return False
