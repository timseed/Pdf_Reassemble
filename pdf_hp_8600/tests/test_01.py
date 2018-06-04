from pdf_hp_8600 import reassemble_scans

from inspect import getsourcefile
from os import chdir, unlink
from os.path import abspath, dirname,exists


class Tester(object):

    def __call__(self, value, expected, message):
        self.description = 'Test {}'.format(message)
        assert value == expected, '{} {}'.format(value, expected)


def test_010():
    rs_obj = reassemble_scans("/users")
    yield Tester(), rs_obj, rs_obj, "reassemble object init ok"


def test_020():
    where_are_we = dirname(abspath(getsourcefile(lambda: 0)))
    try:
        unlink(where_are_we + "/new.pdf")
    except Exception as err:
        pass
    rs_obj = reassemble_scans(where_are_we)
    yield Tester(),  2,  rs_obj.find_finds(), "Check 2 files"
    yield Tester(), True, rs_obj.check_2_scans(), "Check 2 files in directory"
    rs_obj.reassemble(where_are_we+"/new.pdf")
    yield Tester(), True, exists(where_are_we+"/new.pdf"), "New pdf Created"
    yield Tester(), str, type(rs_obj.help()), "Help Function returns a string"



