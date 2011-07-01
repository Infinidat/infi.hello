
import unittest
import mock

class TestCase(unittest.TestCase):
    @mock.patch("__builtin__.print")
    def test_main(self, mock):
        self.assertEquals(mock.called, False)
        from . import main
        main()
        self.assertEquals(mock.called, True)

