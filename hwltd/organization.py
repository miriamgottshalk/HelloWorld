

import workers.structure
from workers.structure import Group
import workers.person


class Employees:
    def __init__(self, empDict):
        if isinstance(empDict, dict):
            self.employeesDict=empDict


class HelloWorld:
    emp = Employees(dict())
    def addWorker(self,curGroup ,worker, name_of_team):
        if curGroup.name==name_of_team:
            curGroup.sub_list.append(worker)
            return
        if curGroup.sub_list!=[]:
            for i in curGroup.sub_list:
                self.addWorker(i ,worker, name_of_team)
    def __init__(self, organizationStruct, path):
                # with open(path) as file:
                # data=file.readLines()
        f = open(path)
        data = f.readlines()
        if True:
            for i in data:
                if i[0]!="#" and i[0]!="\n":
                    l=i.split(",")
                    self.emp.employeesDict[l[3]]=l[0]+" "+l[1]
                    #self.emp.employeesDict.key=l[3]
                    #self.emp.employeesDict.value=l[0]+" "+l[1]
        for i in data:
            temp=object
            if i[0] != "#" and i[0] != "\n":
                l1=i.split(",")
                Add = l1[5].split(";")
                if l1[7]=="staff":
                    if len(Add) == 3:
                       temp=Worker(Person(l1[1], l1[0], l1[2], l1[3], Phone(l1[4].split(":")), PobAddrss(Add[2],Add[0],Add[1])), l1[8])
                    elif len(Add==4):
                        temp=Worker(Person(l1[1], l1[0], l1[2], l1[3], Phone(l1[4].split(":")), StreetAddress(Add[2],Add[3],Add[0],Add[1])), l1[8])
                if l1[7]=="engineer":
                    helper=l1[8].split(";")
                    if len(Add)==3:
                        temp1=Worker(Person(l1[1], l1[0], l1[2], l1[3], Phone(l1[4].split(":")), PobAddrss(Add[2],Add[0],Add[1])), helper[0])
                    elif len(Add)==4:
                        temp1=Worker(Person(l1[1], l1[0], l1[2], l1[3], Phone(l1[4].split(":")), StreetAddress(Add[2],Add[3],Add[0],Add[1])), helper[0])
                        temp=Engineer(temp1,sal[1])
                if l1[7]=="sales":
                    helper=l1[8].split(";")
                    num=len(helper)-1
                    if len(Add)==3:
                        temp3 = Worker(Person(l1[1], l1[0], l1[2], l1[3], Phone(l1[4].split(":")), PobAddrss(Add[2],Add[0],Add[1])), helper[0])
                    elif len(Add)==4:
                        temp3 = Worker(Person(l1[1], l1[0], l1[2], l1[3], Phone(l1[4].split(":")), StreetAddress(Add[2],Add[3],Add[0],Add[1])), helper[0])
                    temp1=helper[1]
                    temp2=helper[1:num]
                    temp=SalesPerson(temp3, temp1, temp2)
                self.addWorker(organizationStruct, temp,l1[6])









