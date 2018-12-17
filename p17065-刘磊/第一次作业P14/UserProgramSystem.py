#实现一个用户管理系统，可以与管理员用户进行交互(本次先不实现验证密码之类的)，根据用户输入的指令(增删改查)，可以进行相应的操作：
#比如 1.输入delete，则让用户输入”用户名”格式字符串，根据用户名查找内存里面的数据，若存在数据则将该数据移除，若用户数据不存在，则提示不存在;
#2.输入update，则让用户输入”用户名:年龄:联系方式”格式字符串，并使用:分隔用户数据，根据用户名查找内存中数据，若存在数据则将改数据更新数据，若用户数据不存在，
#则提示不存在;
#3. 用户输入find，则让用户输入”用户名”格式字符串，根据用户名查找内存中数据包
#含输入字符串的用户信息，并打印;
#4.用户输入list，则打印所有用户信息;打印用户第一个行数据为用户信息描述，从第二行开始为用户数据;
#5.用户输入exit，则提示用户并且保存已经修改的用户信息，退出程序;
#注意：,首次运行时候或者用户为0的时候，需提示用户先添加数据。
#['zhangsan:19:13022103322','lisi:20:13022103322']

'''
author : liulei

'''
userinfo=[] #定义一个空列表存储用户数据
times=0 #首次进入系统

#默认提示用户添加操作员方法
def defaultTips():
    print("no user in this system ！please add one")
    userStr = input("please enter string like 'userName:age:tel':");
    addOrUpdateUser(userStr,"1")
#菜单
def menu():
    print("welcom !")
    print("1.list :see all user !")
    print("2.find :find one user  !")
    print("3.update :update  one user  !")
    print("4.delete :delete one  user  !")
    print("5.exit :exit system !")

#查找所有用户
def getAllUser():
    if len(userinfo):
       for i in userinfo:
           print("userinfo :\n{}".format(i))
    else:
        defaultTips()

#根据用户名查找所有匹配的用户  userName 用户名
def getUser(userName):
    index = -1
    if len(userinfo):
       for i in userinfo:
           if i.find(userName)!=-1:
              print("find one user like :\n{}".format(i))
              index+=1
       if index ==-1:
           print("this user is not  in this system ")
    return index  # 返回找到的元素下标 没找到就返回-1

#修改或添加用户  userstr 用户信息格式化字符串  flag 1：添加 2：修改
def addOrUpdateUser(userstr,flag):
        username=userstr.split(":")[0].strip()#取用户名
        a =getUser(username)
        print(type(a))
        if flag=="1": #添加
            if a != -1:
                print("this user already exists！ please enter new one  or  you want to change this one ? ")
                choice=input("yes or no ? >>>>")
                if choice.lower()=="yes":
                   userinfo[a] = userstr  # 修改用户
                elif(choice.lower()=="no"):
                    print("please enter next step:>>>")
            else:
                   userinfo.append(userstr)  # 添加用户
                   print("add success!")
                   print("please enter next step:>>>")
        else:
            print(type(a))
            if a!=-1:
               userinfo[a]=userstr  #修改用户
            else:
               print("no such user in this system ! \n we will  add this user in system yes or no?")
               choice=input(">>> enter your choice yes or no : ")
               if choice.lower()=="yes":
                     userinfo.append(userstr)  #添加用户
                     print("add success!")

 #删除
def delete(userName):
    if len(userinfo):
        a =getUser(userName)
        if a!=-1:
           #userinfo.remove(userName)  #删除用户
           userinfo.pop(a)  # 删除用户
           print("delete success!")
        else:
            print("no such user in this system ! \n please enter again")
            username=input(">>> enter username which you want to delete: ")
            delete(username)
            print("delete success!")
            if(len(userinfo)==0):
                print("系统内用户已全部删除，请添加一个")
    else:
        defaultTips()

while True:
    if times==0 : #首次进入
        menu()
        times+=1
    options=input("please choice one options! input id >>>>")
    if options == '1':  # 查看所有用户
        getAllUser()
    if options == '2':  # 查找一个用户
        userName=input("please enter userName which you want to find >>>>>");
        getUser(userName)
    if options == '3':  # 修改某个用户
        userStr=input("please enter string like 'userName:age:tel'>>>>>>>>>");
        addOrUpdateUser(userStr,"2")
    if options == '4':  # 删除个用户
        userName = input("please enter userName which you want to delete >>>>>>>>>>>>");
        delete(userName)
    if options=='5':# 退出
        print("thinks !")
        exit()
