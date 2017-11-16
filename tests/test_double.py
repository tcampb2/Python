import sys
import os
sys.path.append(os.path.abspath('../data_structures/LinkedList'))

from parameterized import parameterized
from DoublyLinkedList import LinkedList
from DoublyLinkedList import Link
import unittest.mock as mock
import unittest
        
class DoubleTestCase(unittest.TestCase):
    
    def setUp(self):
    	self._list = LinkedList()
    
    def test_empty(self):
        self.assertTrue(self._list.isEmpty())
    
    @unittest.expectedFailure    
    def test_insert_head_and_remove_head_single_object(self):
    	self._list.insertHead("hello")
    	self.assertEqual(self._list.deleteHead().value, "hello")
    
    @unittest.expectedFailure	
    def test_insert_tail_and_remove_tail_single_object(self):
    	self._list.insertTail("hello")
    	self.assertEqual(self._list.deleteTail().value, "hello")
    
    @unittest.expectedFailure    
    def test_insert_tail_and_remove_head_single_object(self):
    	self._list.insertTail("hello")
    	self.assertEqual(self._list.deleteHead().value, "hello")
    
    @unittest.expectedFailure	
    def test_insert_head_and_remove_tail_single_object(self):
    	self._list.insertHead("hello")
    	self.assertEqual(self._list.deleteTail().value, "hello")
    
    @unittest.expectedFailure
    def test_insert_tail_two_objects(self):
    	self._list.insertTail("hello")
    	self._list.insertTail("hello2")
    	pass
    	
    def test_insert_head_two_objects(self):
    	self._list.insertHead("hello")
    	self._list.insertHead("hello2")
    	pass
    	
    def test_insert_head_then_insert_tail(self):
    	self._list.insertHead("hello")
    	self._list.insertTail("hello2")
    	pass
    	
    @unittest.expectedFailure
    def test_insert_tail_then_insert_head(self):
    	self._list.insertTail("hello")
    	self._list.insertHead("hello2")
    	pass
    
    @unittest.expectedFailure
    def test_insert_tail_and_remove_tail_two_objects(self):
    	self._list.insertTail("hello")
    	self._list.insertTail("hello2")
    	self.assertEqual(self._list.deleteTail().value, "hello2")
    
    @unittest.expectedFailure
    def test_insert_tail_and_remove_head_two_objects(self):
    	self._list.insertTail("hello")
    	self._list.insertTail("hello2")
    	self.assertEqual(self._list.deleteHead().value, "hello")
    
    def test_insert_head_and_remove_head_two_objects(self):
    	self._list.insertHead("hello")
    	self._list.insertHead("hello2")
    	self.assertEqual(self._list.deleteHead().value, "hello2")
    	
    def test_insert_head_and_remove_tail_two_objects(self):
    	self._list.insertHead("hello")
    	self._list.insertHead("hello2")
    	self.assertEqual(self._list.deleteTail().value, "hello")
    
    @parameterized.expand([
        ("test_delete1", "hello", "hello2", "hello3", "hello"),
        ("test_delete2", "hello", "hello2", "hello3", "hello2"),
        ("test_delete3", "hello", "hello2", "hello3", "hello3")])
    def test_delete(self, _, input1, input2, input3, test):
    	self._list.insertHead(input1)
    	self._list.insertHead(input2)
    	self._list.insertHead(input3)
    
    	self._list.delete(test)
    	self.assertRaises(AttributeError, self._list.delete, test)
    	
    @parameterized.expand([
        ("test_string1", "hello", "hello2", "hello3", "hello3 hello2 hello"),
        ("test_string2", "1", "2", "3", "3 2 1"),
        ("test_string3", "top hat", "carrot", "snowman", "snowman carrot top hat")])
    @mock.patch.object(LinkedList, 'display')  
    def test_display(self, _, input1, input2, input3, expected, mock_display):    	
    	def side_effect_list():
        	text = ""
        	current = list.head
        	while(current != None):
        		if(current != list.head):
        			text += " "
        		text += "{}".format(current.value)
        		current = current.next
        	return text
        	
    	mock_display.side_effect = side_effect_list
    	
    	list = LinkedList()
    	
    	list.insertHead(input1)
    	list.insertHead(input2)
    	list.insertHead(input3)
    	
    	self.assertEqual(list.display(), expected)

if __name__ == "__main__":   
	unittest.main()
