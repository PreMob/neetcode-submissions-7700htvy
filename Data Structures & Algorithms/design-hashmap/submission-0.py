class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        idx = self._hash(key)
        for i in self.buckets[idx]:
            if i[0] == key:
                i[1] = value
                return 
        self.buckets[idx].append([key,value])

    def get(self, key: int) -> int:
        idx = self._hash(key)
        for i in self.buckets[idx]:
            if i[0] == key:
                return i[1]

        return -1

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        for i in self.buckets[idx]:
            if i[0] == key:
                self.buckets[idx].remove(i)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)