from pdf_hp_8600 import reassemble_scans

class Tester(object):

    def __call__(self, value, expected, message):
        self.description = 'Test {}'.format(message)
        assert value == expected, '{} {}'.format(value,expected)

def test_010():
    rs_obj = reassemble_scans("/users")
    yield Tester(), rs_obj , rs_obj , "reassemble object init ok"

def test_020():
    rs_obj = reassemble_scans(".")
    rs_obj.find_finds()
    yield Tester(), True, rs_obj.check_2_scans(), "Check 2 files in directory"