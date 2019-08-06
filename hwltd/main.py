import hwltd.organization
from workers.structure import *
from hwltd.organization import HelloWorld
from workers.structure import SalesPerson, Engineer
from hwltd.reports import *

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
    w1=Worker("Trump", "Donnald", 1920, "dtrump@serv.hwltd.com", 567, "Greece;London;4330", 1500)
    g5.sub_list.append(w1)

if __name__ == '__main__':
    main()