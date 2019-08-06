from fractions import Fraction
from workers.person import *

class Group:
    name=""
    description=""
    sub_list=[]
    parents=[]
    allWorkers=[]
    def __init__(self, name, description, parentGroup, sub_list):
        self.name = name
        self.description = description
        self.parentGroup = parentGroup
        self.sub_list=sub_list

    def get_workers(self):
        if self.sub_list!=[]:
            if isinstance(self.sub_list[0], Worker):
                for i in self.sub_list:
                    self.allWorkers.append(i.person1.firstName+" "+i.person1.lastName)
            if isinstance(self.sub_list[0], Group):
                for i in self.sub_list:
                    i.get_workers()
        all_workers=self.allWorkers
        self.allWorkers=[]
        return all_workers

    def get_parents(self):
        while self.parent_group:
            self= self.parent_group
            yield self.name



class Worker:
    def __init__(self, firstName, lastName, yearOfBirth, email, phones, addr, salary):
        self.person1= Person(firstName, lastName, yearOfBirth, email, phones, addr)
        self.salary = salary
    def getSalary(self):
        return self.salary

class Engineer(Worker):
    def __init__(self, firstName, lastName, yearOfBirth, email, phones, addr, salary, bonus):
        self.bonus=bonus
        super(Engineer, self).__init__(firstName, lastName, yearOfBirth, email, phones, addr, salary) #base constructor
    def getSalary(self):
        return self.bonus + self.salary



class SalesPerson(Worker):
    def __init__(self, firstName, lastName, yearOfBirth, email, phones, addr, salary, commission, dealList):
        self.commission = fraction(commission)
        assert isinstance(dealList, list)
        self.deals=dealList
        super(SalesPerson, self).__init__(firstName, lastName, yearOfBirth, email, phones, addr, salary) #base constructor
    deals= []
    def sumOfDeals(self):
        sum=0
        for i in self.deals:
            sum+=i
        return sum
    def getSalary(self):
        return self.salary+self.commission*self.sumOfDeals()

    def main():
        w1 = Worker("sara", "levi", 1999, "sara@mng.hwltd.com", " 0527617201", "addr",34000)
        w2 = Worker("rivka", "cohen", 2000, "rivka@mng.hwltd.com", " 052761111", "addr", 5000)
        w3 = Worker("rachel", "shabtai", 2001, "rachel@mng.hwltd.com", " 112345566", "addr", 6000)
        w4 = Worker("lea", "polak", 2002, "lea@mng.hwltd.com", " 987654321", "addr", 7000)
        e = Engineer("tamar", "shalev", 1999, "sara@mng.hwltd.com", " 0527617201", "addr", 4000, 50)
        sp = SalesPerson("rivka", "cohen", 2000, "rivka@mng.hwltd.com", " 052761111", "addr", 5000, 0.1, [1, 1, 1])
        g1 = Group("asd", "wer", None, [w1, w2])
        g2 = Group("aaa", " bbb", None, [w3, w4])
        g3 = Group("bbb", " ccc", list1, [g1, g2])
        g4 = Group("awe", "" ,None, [g1,g2])
        print(g1.get_workers())
        print(g2.get_workers())
        print(g3.get_workers())
        print(g3.get_parents())
        print(g4.get_workers())
        print(w1.getSalary())
        print(e.getSalary())
        #print(sp.sumOfDeals())
        #print(sp.commission)
        #print(sp.getSalary())

    if __name__ == '__main__':
        main()
    print("finish")