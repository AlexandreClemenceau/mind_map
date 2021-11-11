import unittest
import main

class TestStringMethods(unittest.TestCase):
    def test_create(self):
        self.assertTrue(main.create_child('test1', {}))

    def test_search(self):
        self.assertFalse(main.search_child('node1', {}))
        self.assertTrue(main.search_child('node1', main.create_child('node1', {})))

    def test_del(self):
        self.assertTrue(main.del_child('node1', main.create_child('node1', {})))
        self.assertFalse(main.del_child('node1', main.create_child('node2', {})))

    def test_update(self):
        node = main.create_child('node1', {})
        self.assertTrue(main.update_child('node1', 'node11', node))
        node = main.create_child('node1', {})
        self.assertFalse(main.update_child('node2', 'node11', node))

if __name__ == '__main__':
    unittest.main()