from typing import NewType
from LinkedList import LinkedList


class HashTable:

    def __init__(self, size):
        self.size = size
        self.arr = self.create_arr(size)

    # 1️⃣ TODO: Complete the create_arr method.

    # Each element of the hash table (arr) is a linked list.
    # This method creates an array (list) of a given size and populates each of its elements with a LinkedList object.

    def create_arr(self, size):

        array = []

        for i in range(size):
            new_list = LinkedList()
            array.append(new_list)
        return array

    # 2️⃣ TODO: Create your own hash function.

    # Hash functions are a function that turns each of these keys into an index value that we can use to decide where in our list each key:value pair should be stored.

    def hash_func(self, key):
        start_letter = key[0].upper()
        distance_from_start = ord(start_letter) - ord('A')

        index = distance_from_start % self.size
        return index

    # 3️⃣ TODO: Complete the insert method.

    # Should insert a key value pair into the hash table, where the key is the word and the value is a counter for the number of times the word appeared. When inserting a new word in the hash table, be sure to check if there is a Node with the same key in the table already.

    def insert(self, key, value):
        key_hash = self.hash_func(key)

        # new tuple for items
        new_items = (key, value)

        new_ll = self.array[key_hash].find(new_items)
        if new_ll == -1:
            self.array[key_hash].append(new_items)

            # 4️⃣ TODO: Complete the print_key_values method.

            # Traverse through the every Linked List in the table and print the key value pairs.

            # For example:
            # a: 1
            # again: 1
            # and: 1
            # blooms: 1
            # erase: 2

    def print_key_values(self):
        for new_ll in self.arr:
            new_ll.print_nodes()
