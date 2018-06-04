# pdf Reassemble

I recently had to scan a rather long document in, only to find that the super posh hp8600 only did single sided scanning.

The 8600 Pro scanner, does not allow you to do double sided scanning. Which is a shame as its double sided printing is excellent.

Instead what you need to do is as follows.

  - Get the Pages nicely stacked together and place them on the top of the scanner. 
  - Put a USB Drive (Win32 or maybe ntfs) into the printer
  - Put the Documents on the top of the scanner - in the scanner feeder
  - Using the front screen, Right Arrow - Select Scan - then select the Green Button Scan.
  - When all the documents are done....
  - Rotate the documents 180 degrees and put them back in the scanner. Do not turn them head over heels - just rotatoe them 180 Degrees
  - Press Scan for the 2nd time.
  
At the end of this (wait for the scan to finish) - and then pull out the USB drive.

You should find 2 pdf documents

## The Two Pdf documents

The first will have pages (1,3,5,7,9) on it.... then 2nd will have pages (10,8,6,4,2)

This script will make the new_document have pages in the order of (1,2,3,4,....)

## Using the Module

This is a sample of how you need to use this Package

```python
from pdf_hp_8600 import reassemble_scans
rs = reassemble_scans("Directory_where_2_pdfs_live")
rs.find_finds()
rs.reassemble("/tmp/new_document.pdf")
```

# Requirements

You need the following python modules

     PyPDF2
     daiquiri
     
You can rip out the daiquiri if you need (I just like decent logging), but you need the PyPDF2.

# Tested 

Testing using nose, coverage, and pylint

Coverage is 89% 
Link has only minor warnings.

There is a test folder, with the tests in it should you wish to try these on your own.

Developed and tested on

  - Mac 
  - Ubuntu 18
  - Python 3.6
  
  