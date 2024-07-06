
class HashTable:
    def __init__(self, size=10) -> None:
        self.size = size
        self.table = [None] * size
                                                                                                                           
    def hash_function(self, key):
        hashed = 0
        hashed = sum(ord(char) for char in key)
        return hashed%self.size
    
    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = []
        
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return 'Key already exist, value added'
        self.table[index].append([key, value])

    
    def get(self, key):
        index = self.hash_function(key)
        if self.table[index] is None:
            return None
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1], f'found at {index}'
        return None
    
    def display(self):
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f'index {i}: {bucket}')
            else:
                print(f'index {i}: Empty')


    
hashed = HashTable()
hashed.insert('aa','aer')
hashed.insert('ab','asdsd')
hashed.insert('ac','asdsd')
hashed.insert('ad','asdsd')
hashed.insert('bb','aweq')
hashed.insert('cc','asdw')
hashed.display()
print(hashed.get('ac'))
