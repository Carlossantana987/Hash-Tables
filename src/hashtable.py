# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.
        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        hash = 0

        for char in str(key):
            hash += ord(char)
        return hash % self.capacity


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        key_hash = self._hash(key)
        print(f"key hash:{key_hash}")
        key_value = [key, value]
        print(f"key value:{key_value}")
        print(f"self.storage[key hash]:{self.storage[key_hash]} \n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


        if self.storage[key_hash] is None:
            self.storage[key_hash] = list([key_value])
            return
        else:
            for pair in self.storage[key_hash]:
                print(f"pair[0]:{pair[0]}")
                print(f"pair[1]:{pair[1]}\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                if pair[0] == key:
                    pair[1] = value
                    return
            self.storage[key_hash].append(key_value)
            return


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''

        key_hash = self._hash(key)

        if self.storage[key_hash] is None:
            return "Key Not Found"
        for i in range(0,len(self.storage[key_hash])):
            if self.storage[key_hash][i][0] == key:
                self.storage[key_hash].pop(i)
                return



    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        key_hash = self._hash(key)

        if self.storage[key_hash] is not None:
            for pair in self.storage[key_hash]:
                if pair[0] == key:
                    return pair[1]

        return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        new_storage = [None] * (len(self.storage) * 2)

        for i in range(len(self.storage)):
            new_storage[i] = self.storage[i]

        self.storage = new_storage



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
