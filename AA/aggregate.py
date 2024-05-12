class AggregateStack:
    def __init__(self):
        self.stack = []
        self.cost = 0
    def push(self,item):
        self.stack.append(item)
        self.cost += 1
        self.prints()
    def pop(self):
        self.stack.pop()
        self.cost += 1
        self.prints()
    def multipop(self,k):
        for i in range(0,k):
            self.pop
    def prints(self):
        print(f"{self.stack}\nCost {self.cost}\n")


#Dynamic
def aggregate(n):
    size = 1
    dcost = 0
    icost = 0
    total = 0
    totalcost = 0

    for i in range(1,n+1):
        icost = 1
        if i > size:
            size = size*2
            dcost = i-1
        total = icost+dcost
        totalcost += total
        print(f"{i}\t\t{dcost}\t\t{icost}\t\t{total}\t\t\t{totalcost}")
        icost = 0
        dcost = 0
    return totalcost/n

a = aggregate(5)
print(a)

        