import os
filename = 'student.txt'
def main():
    while True:
        menu()
        choice = int(input("请选择"))
        if choice in [0,1,2,3,4,5,6,7]:
            if choice == 0:
                answer = input('您确定要退出系统吗y/n')
                if answer=='y' or answer=='Y':
                    print("谢谢您的使用")
                    break
                else:
                    continue
            elif choice == 1:
                insert()
            elif choice ==2:
                search()
            elif choice ==3:
                delete()
            elif choice ==4:
                modify()
            elif choice ==5:
                sort()
            elif choice ==6:
                total()
            elif choice ==7:
                show()
def menu():
    print("========================学生信息管理系统========================")
    print("----------------------------功能菜单---------------------------")
    print("\t\t\t1.录入学生信息")
    print("\t\t\t2.查找学生信息")
    print("\t\t\t3.删除学生信息")
    print("\t\t\t4.修改学生信息")
    print("\t\t\t5.排序")
    print("\t\t\t6.统计学生总人数")
    print("\t\t\t7.显示所有学生信息")
    print("\t\t\t0.exit")
    print("--------------------------------------------------------------")

def insert():
    student_lst=[]
    while True:
        id = input("请输入ID（如1001）：")
        if not id:
            break
        name = input("请输入姓名（如小周）：")
        if not name:
            break
        try:
            englist = int(input("请输入英语成绩："))
            python = int(input("请输入python成绩："))
            java = int(input("请输入java成绩："))
        except:
            print("输入无效，请重新输入")
            continue
        #将录入的信息保存到字典
        student={'id':id,'name':name,'englist':englist,'python':python,'java':java}
        student_lst.append(student)
        answer =input("是否继续添加？y/n\n")
        if answer == 'n' or answer == 'N':
            break
    save(student_lst)
    print('学生信息录入完毕')
def save(lst):
    try:
        stu_txt = open(filename,'a',encoding='utf-8')
    except:
        stu_txt = open(filename,'w',encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()
    
def search():
    student_query=[]
    while True:
        if os.path.exists(filename):
            stuid=''
            name=''
            choice = int(input("根据id查询请输入1，根据name查询请输入2"))
            if choice == 1:
                stuid = input("请输入要查找的学生id：")
            elif choice== 2:
                name = input("请输入学生的姓名")
            else:
                print("输入有误，请重新输入")
                search()
            with open(filename,'r',encoding='utf-8') as file:
                student_oldlst = file.readlines()
                for item in student_oldlst:
                    d = dict(eval(item))
                    if d['id']==stuid or d['name']==name:
                        student_query.append(d)
            show_student(student_query)
            #清空列表
            student_query.clear()
            answer = input("是否要继续查询？y/n\n")
            if answer=='y':
                continue
            else:
                break
                        
        else:
            print("没有学生信息")
            return
def show_student(lst):
    if len(lst)==0:
        print("没有查询到学生信息，无数据显示")
        return
    format_title='{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format('ID','姓名','英语成绩','Python成绩','Java成绩','总成绩')) 
    format_data='{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'  
    for item in lst:
        print(format_data.format(item.get('id'),
                                 item['name'],
                                 item['englist'],
                                 item['python'],
                                 item['java'],
                                 str(int(item['englist'])+int(item['python'])+int(item['java']))
                                 )) 
def delete():
    while True:
        id=input("请输入要删除的学生的ID")
        if id != "":
            if os.path.exists(filename):
                with open(filename,'r') as file:
                    student_old = file.readlines()
            else:
                student_old = []
            flag = False
            if student_old:
                with open(filename,'w',encoding='utf-8') as wfile:
                    d={}
                    for item in student_old:
                        d=dict(eval(item))
                        if d['id'] != id:
                            wfile.write(str(d)+'\n')
                        else:
                            flag = True
                    if flag:
                        print("id为{}的学生信息成功删除".format(id))
                    else:
                        print("id为{id}的学生信息不存在")
            else:
                print("无学生信息")
                break
            show()      #删除后重新显示所有学生信息
            answer = input("是否继续删除？y/n\n")
            if answer == 'n' or answer =='N':
                break                   
def modify():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as mfile:
            student_oldlst = mfile.readlines()
                                    
    else:
        return
    stuid=input("请输入要修改的学生id：")
    with open(filename,'w',encoding='utf-8') as wfile:
        for item in student_oldlst:
            d = dict(eval(item))
            if d['id'] == stuid:
                print('找到学生信息，可以修改他的相关信息了')
                while True:
                    try:
                        d['name'] = input('请输入姓名：')
                        d['englist'] = input('请输入英语成绩：')
                        d['python'] = input('请输入python成绩：')
                        d['java'] = input('请输入java成绩：')
                    except:
                        print("您的输入有问题请重新输入")
                    else:
                        break
                wfile.write(str(d)+'\n')
                print("修改成功")
            else:
                wfile.write(str(d)+'\n')
    ans = input("是否修改其他学生信息y/n\n")
    if ans == 'y':
        modify()
    else: 
        show()
def sort():
    student_lst=[]
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as file:
            student=file.readlines()
        for item in student:
            student_lst.append(dict(eval(item)))
        asc_or_desc = int(input("请选择（0:升序，1:降序）："))
        mode = input('请选择排序方式1.按英语成绩排序 2.按Python成绩排序 3. 按Java成绩排序 4. 按总成绩排序：')
        if mode =='1':
            student_lst.sort(key=lambda student:int(student['englist']),reverse=asc_or_desc)
        elif mode =='2':
            student_lst.sort(key=lambda student : int(student['python']),reverse=asc_or_desc)
        elif mode == '3':
            student_lst.sort(key=lambda student : int(student['java']),reverse=asc_or_desc)
        elif mode == '4':
            student_lst.sort(key=lambda student : int(student['englist'])+int(student['python'])+int(student['java']),reverse=asc_or_desc)
        else:
            print('请重新输入')
            sort()
        show_student(student_lst)        
    else:
        return
def total():
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as file:
            students = file.readlines()
            if students:
                print(f'一共有{len(students)}名学生')
            else:
                print(f'还没有学生数据')
    else:
        print("暂无学生数据")
def show():
    student_lst=[]
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as file:
            student = file.readlines()
            for item in student:
                student_lst.append(eval(item))
            if student_lst:
                show_student(student_lst)
            
    else:
        print('没有学生信息')
        return
if __name__=='__main__':
    main()