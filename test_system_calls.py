import unittest2
from nose.tools import *
from mock import patch

from dockerplace.system_calls import get_imageid
from dockerplace.system_calls import get_all_actions
from dockerplace.system_calls import get_container_actions
from dockerplace.system_calls import get_containers
from dockerplace.system_calls import run_make_action


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

    @patch("dockerplace.system_calls.isfile")
    @patch("dockerplace.system_calls.do_run")
    def test_simple_(self, mock_run, mock_file):
        """get_container_actions should return a list of the available actions"""
        expect = ["actiona", "actionb"]
        stub = "\n".join(expect)
        mock_file.return_value = True
        mock_run.side_effect = [
            stub
            ]
        result = get_container_actions("fake/path")
        mock_run.called
        self.assertEqual(result, expect)


class test_get_containers(BaseTest):
    def test_empty_param_raises(self):
        """an empty parameter raises an exception"""
        self.assertRaises(TypeError, get_containers)

################################################################################

class test_get_all_actions(BaseTest):
    def test_empty_param_raises(self):
        """an empty parameter raises an exception"""
        self.assertRaises(TypeError, get_all_actions)

    @patch("dockerplace.system_calls.get_imageid")
    @patch("dockerplace.system_calls.get_container_actions")
    @patch("dockerplace.system_calls.get_containers")
    def test_actions_are_reported(self, m_gc, m_gca, m_gii):
        """it just reports the actions as given"""
        # mock as hell. proof of bad design
        m_gc.return_value = ["uno","dos","tes"]
        m_gca.side_effect = [["aa","ab"], ["ba","bb"], ["ca","cb"]]
        m_gii.side_effect = ["pic1.png","pic2.png","pic3.png"]
        expectations = [
            {'image': 'pic1.png', 'name': 'uno', 'actions': ['aa', 'ab']},
            {'image': 'pic2.png', 'name': 'dos', 'actions': ['ba', 'bb']},
            {'image': 'pic3.png', 'name': 'tes', 'actions': ['ca', 'cb']}
            ]

        # run something, for mocks sake
        results = get_all_actions("foo")
        eq_(results, expectations)
        assert m_gca.called is True
        assert m_gc.called is True
        assert m_gii.called is True

################################################################################

class test_run_make_action(BaseTest):
    def test_empty_param_raises(self):
        """an empty parameter raises an exception"""
        self.assertRaises(TypeError, run_make_action)

    @patch("dockerplace.system_calls.do_run")
    def test_it_runs(self, mymock):
        """run_make_action should return the output of running an action"""
        stub = "this is output"
        mymock.return_value = stub
        eq_(stub, run_make_action("home/docker","dockerapp","action"))
        call = "cd home/docker/dockerapp; make action"
        mymock.assert_called_with(call)
