#Accounting method
# Dynamic table
def accounting(n):
    size = 1
    total = 0
    bank = 0
    icost = 0
    dcost = 0
    for i in range(1,n+1):
        icost = 1
        if i > size:
            size = size*2
            dcost = i-1
        total = icost + dcost 
        bank += (3-total)
        print(f"{i}\t\t\t{icost}\t\t{dcost}\t\t\t{total}\t\t\t{bank}")
        icost = 0
        dcost = 0
# accounting(1025)


class AccountingStack:
    def __init__(self):
        self.stack = []
        self.cost = 0
        self.balance = 0
    def push(self,item):
        self.stack.append(item)
        self.cost += 1
        self.balance += 1
        self.printstack()
    def pop(self):
        self.stack.pop()
        self.cost += 1
        self.balance -= 1
        self.printstack()
    def multipop(self,k):
        for i in range(k):
            self.pop()
    def printstack(self):
        print(self.stack,"\nBalance",self.balance,"\n")


s = AccountingStack()
s.push(10)
s.push(20)
s.push(30)
s.pop()
s.multipop(2)        
print(f"Amortized Cost {s.cost/6}")
