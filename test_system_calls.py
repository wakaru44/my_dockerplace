import unittest2
from mock import patch

from dockerplace.system_calls import get_imageid
from dockerplace.system_calls import get_all_actions
from dockerplace.system_calls import get_container_actions
from dockerplace.system_calls import get_containers


class BaseTest(unittest2.TestCase):
    def setUp(self):
        pass


class test_get_imageid(BaseTest):
    def setUp(self):
        # create some stubs
        pass

    def test_empty_param_raises(self):
        """an empty parameter raises an exception"""
        self.assertRaises(TypeError, get_imageid)


class test_get_container_actions(BaseTest):
    def test_empty_param_raises(self):
        """an empty parameter raises an exception"""
        self.assertRaises(TypeError, get_container_actions)

    @patch("fabric.api.local")
    def test_simple_(self, mymock):
        """it sholud return a list of the available actions"""
        expect = ["actiona", "actionb"]
        mymock.side_effect = "\n".join(expect)
        self.assertEqual(get_container_actions("fake/path"), expect)


class test_get_containers(BaseTest):
    def test_empty_param_raises(self):
        """an empty parameter raises an exception"""
        self.assertRaises(TypeError, get_containers)


class test_get_all_actions(BaseTest):
    def test_empty_param_raises(self):
        """an empty parameter raises an exception"""
        self.assertRaises(TypeError, get_all_actions)
