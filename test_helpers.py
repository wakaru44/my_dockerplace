import unittest2
from mock import patch

from dockerplace.helpers import is_there_makefile


class BaseTest(unittest2.TestCase):
    def setUp(self):
        pass


class test_is_there_makefile(BaseTest):
    def test_return_false_onempty(self):
        assert is_there_makefile() is not True
        assert is_there_makefile("") is not True

    def test_return_true_on_existing(self):
        stub = "yes\nthere\nis\nMakefile\nhere"
        assert is_there_makefile(stub) is True
