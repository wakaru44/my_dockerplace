import unittest2
from nose.tools import *
from mock import patch

from dockerplace.helpers import is_there_makefile
from dockerplace.helpers import parse_make
from dockerplace.helpers import sanitize


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


class test_parse_make(BaseTest):
    def test_return_empty_on_empty(self):
        eq_(parse_make(""), [])

    def test_return_only_firest(self):
        """ if there are semi-colons, forget it"""
        stub = "things\nwith\nnewlines"
        eq_(parse_make(stub), ["things", "with", "newlines"])


class test_sanitize(BaseTest):
    def test_return_empty_on_empty(self):
        eq_(sanitize(""), "")

    def test_return_only_firest(self):
        """ if there are semi-colons, forget it"""
        stub = "command;with;semicolons"
        eq_(sanitize(stub), "command")
