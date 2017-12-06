from parameterized import parameterized
import unittest.mock as mock
import unittest
import sys
import os

sys.path.append(os.path.abspath('../data_structures/LinkedList'))
from singly_LinkedList import Linked_List
from singly_LinkedList import Node

class SingleTestCase(unittest.TestCase):

    def setUp(self):
        self._list = Linked_List()
       
    def test_empty(self):
        self.assertTrue(self._list.isEmpty())
            
    def test_insert_head_and_remove_head_single_object(self):
    	self._list.insert_head("hello")
    	self.assertEqual(self._list.delete_head().data, "hello")
    	
    def test_insert_tail_and_remove_tail_single_object(self):
    	self._list.insert_tail("hello")
    	self.assertEqual(self._list.delete_tail().data, "hello")
        
    def test_insert_tail_and_remove_head_single_object(self):
    	self._list.insert_tail("hello")
    	self.assertEqual(self._list.delete_head().data, "hello")
    
    def test_insert_head_and_remove_tail_single_object(self):
    	self._list.insert_head("hello")
    	self.assertEqual(self._list.delete_tail().data, "hello")
    	
    def test_insert_head_two_objects(self):
    	self._list.insert_head("hello")
    	self._list.insert_head("hello2")
    	pass
    
    def test_insert_tail_one_object(self):
    	self._list.insert_head("hello")
    	pass
    	
    def test_insert_tail_two_objects(self):
    	self._list.insert_tail("hello")
    	self._list.insert_tail("hello2")
    	pass

    @parameterized.expand([
        ("test_string1", "hello", "hello2", "hello3", "hello3 hello2 hello"),
        ("test_string2", "1", "2", "3", "3 2 1"),
        ("test_string3", "top hat", "carrot", "snowman", "snowman carrot top hat")])
    @mock.patch.object(Linked_List, 'printList')  
    def test_display(self, _, input1, input2, input3, expected, mock_display):    	
    	def side_effect_list():
        	text = ""
        	tamp = list.Head
        	while(tamp != None):
        		if(tamp != list.Head):
        			text += " "
        		text += "{}".format(tamp.data)
        		current = tamp.next
        	return text
        	
    	mock_display.side_effect = side_effect_list
    	
    	list = Linked_List()
    	
    	list.insert_head(input1)
    	list.insert_head(input2)
    	list.insert_head(input3)
    	
    	self.assertEqual(list.printList(), expected)

if __name__ == "__main__":   
	unittest.main()