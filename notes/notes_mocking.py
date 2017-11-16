from data_structures.LinkedList.DoublyLinkedList import LinkedList
from data_structures.LinkedList.DoublyLinkedList import Link
import unittest.mock as mock
import unittest
        

class DoubleTestCase(unittest.TestCase):

        
    def test_empty(self):
        list = LinkedList()
        self.assertTrue(list.isEmpty())
        
    @mock.patch('data_structures.LinkedList.DoublyLinkedList.LinkedList')
    def test_insertHead(self, mock_list):
    	mock_list.insertHead("hello")
    	self.assertTrue(mock_list.insertHead.called_once_with("hello"))
        
	
    @mock.patch.object(Link, 'displayLink') 
    @mock.patch.object(LinkedList, 'display') 
    def test_display(self, mock_display, mock_link_display):
    	list_of_return_values= ["hello", "hello2", "hello3"]
    	
    	def side_effect_link():
        	return list_of_return_values.pop()
    
    	mock_link_display.side_effect = side_effect_link
    	
    	def side_effect_list():
        	text = ""
        	current = list.head
        	while(current != None):
        		if(current != list.head):
        			text += " "
        		text += "{}".format(current.displayLink())
        		current = current.next
        	return text
    	mock_display.side_effect = side_effect_list
    	
    	list = LinkedList()
    	
    	list.insertHead("hello")
    	list.insertHead("hello2")
    	list.insertHead("hello3")
    	
    	self.assertEqual(list.display(), "hello3 hello2 hello")


if __name__ == "__main__":   
	unittest.main()
