from LinkedList import LinkedList

class HashTable:

  def __init__(self, size):
    self.size = size
    self.arr = self.create_arr(size)

  # Each element of the hash table (arr) is a linked list.
  # This method creates an array (list) of a given size and populates each of its elements with a LinkedList object.
  def create_arr(self, size):
    new_array = []

    for index in range(size):
      new_linked_list = LinkedList()
      new_array.append(new_linked_list)
    
    return new_array



  # Hash functions are a function that turns each of these keys into an index value that we can use to decide where in our list each key:value pair should be stored. 
  def hash_func(self, key):
    index = 1

    for char in key:
        index = index * 17
      
    return index % self.size



  # Should insert a key value pair into the hash table, where the key is the word and the value is a counter for the number of times the word appeared. When inserting a new word in the hash table, be sure to check if there is a Node with the same key in the table already.
  def insert(self, key, value):
    data = (key, value)
    arr_index = self.hash_func(key)
    linked_list = self.arr[arr_index]
    linked_list_index = linked_list.find(key)

    if linked_list_index == -1:
      linked_list.append(data)
    
    else:
      linked_list.update(key)



  # Traverse through the every Linked List in the table and print the key value pairs.
  # For example: 
  # a: 1
  # again: 1
  # and: 1
  # blooms: 1
  # erase: 2
  def print_key_values(self):
    for linked_list in self.arr:
      linked_list.print_nodes()
    



