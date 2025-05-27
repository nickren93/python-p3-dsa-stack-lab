class Stack:

    def __init__(self, items = [], limit = 100):
        #pass
        self.items = []
        self.limit = limit
        for element in items:
            self.items.append(element)

    def isEmpty(self):
        #pass
        if len(self.items) == 0:
            return True
        else:
            return False

    def push(self, item):
        #pass
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            return "Stack overflow"

    def pop(self):
        #pass
        if len(self.items) > 0:
            return self.items.pop()

    def peek(self):
        #pass
        return self.items[-1]
    
    def size(self):
        #pass
        return len(self.items)

    def full(self):
        #pass
        if len(self.items) == self.limit:
            return True
        else:
            return False

    def search(self, target):
        #pass
        if target in self.items:
            if self.items.index(target) == (self.size()-1):
                return 0
            else:
                return (self.size()-1) - self.items.index(target)
        else:
            return -1