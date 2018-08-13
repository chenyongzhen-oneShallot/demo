#coding=utf-8
import sys,getpass,os
#os.system('clear')
i=0
while i<3:
    name=input("请输入姓名:")
    lock_file=open('account_lock','r+')
    lock_list=lock_file.readlines()

    for lock_line in lock_list:
        lock_line=lock_line.strip('\n')
        if name==lock_line:
            sys.exit('用户%s已被锁定，退出' % name)

    user_file=open('account','r')
    user_list=user_file.readlines()
    for user_line in user_list:
        (user,password)=user_line.strip('\n').split()
        if name==user:
            j=0
            while j<3:
                pwd=input("请输入密码：")
                if pwd==password:
                    print("登陆成功，用户%s" % name)
                    sys.exit(0)
                else:
                    if j!=2:
                        print("密码错误，请重试，还有%d次机会" %(2-j))
                j+=1
            else:
                lock_file.write(name+'\n')
                sys.exit("用户%s达到最大登录次数，将被锁定并退出" % name)
        else:
            pass
    else:
        if i!=2:
            print("用户名不存在，请重试，还有%d次机会" %(2-i))
    i+=1
else:
    sys.exit('用户%s不存在，退出' % name)

lock_file.close()
user_file.close()


