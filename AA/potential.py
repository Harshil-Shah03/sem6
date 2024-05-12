class Potential:
    def __init__(self):
        self.stack = []
        self.size = 0
    
    def push(self,item):
        Amortized_cost = 0
        self.stack.append(item)
        Amortized_cost += 1+len(self.stack)-self.size
        self.size += 1
        return f"Amortized Cost{Amortized_cost}"

    def pop(self):
        Amortized_cost = 0
        self.stack.pop()
        Amortized_cost += 1+len(self.stack)-self.size
        self.size -= 1
        return f"Amortized Cost{Amortized_cost}"
    
    def multipop(self,k):
        Amortized_cost = 0
        for i in range(k):
            self.pop()
        Amortized_cost += k+len(self.stack)-self.size
        self.size -= k
        return f"Amortized Cost{Amortized_cost}"
    
s = Potential()
print(s.push(20))
print(s.push(30))
print(s.pop())
s.push(40)
s.push(40)
s.push(40)
s.push(39)
print(s.multipop(2))