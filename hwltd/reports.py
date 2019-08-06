"""
def main():
    g1 = Group("Hello World", "", None, [])
    g2 = Group("Engineering Department", "", None, [])
    g3 = Group("SW Group", "", None, [])
    g4 = Group("Infrastructure Team", "", None, [])
    g5 = Group("App Team", "", None, [])
    g6 = Group("Drivers Team", "", None, [])
    g7 = Group("QA Team", "", None, [])
    g8 = Group("HW Group", "", None, [])
    g9 = Group("Chip Team", "", None, [])
    g11 = Group("Board Team", "", None, [])
    g12 = Group("Power Team", "", None, [])
    g13 = Group("CTO Group", "", None, [])
    g14 = Group("System Group", "", None, [])
    g15 = Group("Design Team", "", None, [])
    g16 = Group("Poc Team", "", None, [])
    g17 = Group("HR Department", "", None, [])
    g18 = Group("Recruitment Group", "", None, [])
    g19 = Group("Tech Team", "", None, [])
    g20 = Group("Staff Team", "", None, [])
    g21 = Group("Culture Group", "", None, [])
    g22 = Group("Finance Department", "", None, [])
    g23 = Group("Salaries Group", "", None, [])
    g24 = Group("Budget Group", "", None, [])
    g25 = Group("Income Team", "", None, [])
    g26 = Group("Outcome Team", "", None, [])
    g1.sub_list.append(g2)
    g1.sub_list.append(g17)
    g1.sub_list.append(g22)
    g2.parentGroup=g1
    g2.sub_list.append(g3)
    g2.sub_list.append(g8)
    g2.sub_list.append(g13)
    g2.sub_list.append(g14)
    g3.sub_list.append(g4)
    g3.sub_list.append(g5)
    g3.sub_list.append(g6)
    g3.sub_list.append(g7)
    g3.parentGroup = g2
    g4.parentGroup=g2
    g5.parentGroup=g2
    g6.parentGroup = g2
    g7.parentGroup = g2
    g8.parentGroup=g2
    g8.sub_list.append(g9)
    g8.sub_list.append(g11)
    g8.sub_list.append(g12)
    g9.parentGroup=g8
    g11.parentGroup = g8
    g12.parentGroup = g8
    g13.parentGroup=g2
    g14.parentGroup=g2
    g14.sub_list.append(g15)
    g14.sub_list.append(g16)
    g15.parentGroup=g14
    g16.parentGroup = g14
    g17.parentGroup=g1
    g17.sub_list.append(g18)
    g17.sub_list.append(g21)
    g18.parentGroup=g17
    g18.sub_list.append(g19)
    g18.sub_list.append(g20)
    g19.parentGroup=g18
    g20.parentGroup = g18
    g21.parentGroup=g17
    g22.parentGroup=g1
    g22.sub_list.append(g23)
    g22.sub_list.append(g24)
    g23.parentGroup=g22
    g24.parentGroup=g22
    g24.sub_list.append(g25)
    g24.sub_list.append(g26)
    g25.parentGroup=g24
    g26.parentGroup = g24
    Hello_world=g1
    h=HelloWorld(Hello_world,'C:/Users/rent/PycharmProjects/untitled/prework-task2-data.txt')

if __name__ == '__main__':
    main()

def get_num_emploees(department, depth):
    assert isinstance(department, Group)
    print ("*********depatment******")
    for worker in department.get_workers():
        print (worker)
    print ("*********************")
    num_of_workers_in_department = len(department.get_workers())
    print("{0} - {1}".format(department.name, num_of_workers_in_department))
    if depth == 1:
        return len(department.get_workers())
    num_of_workers_in_group = 0
    for group in department.sub_list:
        print("*********group******")
        if group.get_workers() is not None:
            for worker in group.get_workers():
              print(worker.person.last_name)
        print("*********************")
        num_of_workers_in_group = len(group.get_workers())
        print("{0} - {1}".format(group.name, num_of_workers_in_group))
        if depth == 2:
            return len(group.get_workers())
        for team in group.sub_list:
            print("*********team******")
            if team.get_workers() is not None:
              for worker in team.get_workers():
                 print(worker.person.last_name)
            print("*********************")
            num_of_workers_in_team = len(team.get_workers())
            print("{0} - {1}".format(team.name, num_of_workers_in_team))
            return len(team.get_workers())
"""

import hwltd.organization
from workers.structure import Group
from hwltd.organization import HelloWorld
from workers.structure import*


flag=True




class reports:
    sum1=0
    counter = 0
    def get_num_employees(self,department, depth):
        self.print_depth(department, depth)

    def print_depth(self,dep_group, depth, space=""):
        global sum1
        global counter
        if dep_group.sub_list!=[]:
            if isinstance(dep_group.sub_list[0], Worker):
                length=len(dep_group.sub_list)
                if(depth!=0):
                    print(space+dep_group + "-" + length + " workers")
                return int(length)
            else:
                for i in dep_group.sub_list:
                    if depth!=0:
                        space=space+"   "
                        helper=self.print_depth(i, depth-1, space)
                        self.sum1=helper+self.sum1
                        print(space+dep_group.name+"-"+str(self.sum1)+" workers")


    def searchGroup(self,dep,group):
        if group.name==dep:
            return group
        else:
            for i in group.sub_list:
                return searchGroup(dep,i)


    def searchTeam(self,worker, group):
        if isinstance(group.sub_list, Worker):
            return None
        if worker in group.sub_list:
            print((group.name))
            return group
        else:
            for i in group.sub_list:
                searchTeam(worker, i)
                print((group.name))

    def get_relational_salary(self,worker):
        teamDict=dict()
        assert isinstance(worker, Worker)
        for i in searchTeam(HelloWorld.Hello_world, worker).sub_list:
            if i!=worker:
                teamDict[i.name]=i.salary/worker.getSalary


    def get_average_salary(self,group):
        assert isinstance(group, Group)
        if isinstance(group.sub_list[0], (Worker, SalesPerson, Engineer)):
            for i in group.sub_list:
                sum1+=i.salary
                counter+=1
            return
        if isinstance(group.sub_list[0], Group):
            for i in group.sub_list:
                get_average_salary(i)
        return  sum1/counter

