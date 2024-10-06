from login_singin import *
from data import *
from admin import *
from user import *
while True:
    print('''
    1.Register as new
    2 login
    3.exit''')

    c=int(input('Enter your choice : '))
    if c==1:
        register()
    elif c==2:
        f,u=login()

# ---------------------- ADMIN LOGIN ---------------------------
        
        if f==1:
            while True:
                print('''
                1.Staff
                2.View Staff
                3.View Users
                4.exit''')
                c=int(input('enter your choice : '))
                if c==1:
                    while True:
                        print('''
                        1.Add Staff
                        2.Update staff salary
                        3.delete staff
                        4.exit''')
                        c1=int(input('enter your choice : '))
                        if c1==1:
                            add_stf()
                        elif c1==2:
                            up_sal()
                        elif c1==3:
                            del_stf()
                        elif c1==4:
                            break
                        else:
                            print('invalid choice')
                elif c==2:
                    view_staff()
                elif c==3:
                    view_usr()
                elif c==4:
                    break
                else:
                    print('invalid choice')

# ---------------------- ADMIN END ------------------------------
        
#-------------------------- USER LOGIN ------------------------------
        
        if f==2:
            while True:
                print('''
                    1.View Profile
                    2.Add money
                    3.Withdraw money
                    4.Statement
                    5.Send money(upi)
                    6.Update Profile
                    7.exit''')
                c= int(input('enter your choice: '))
                if c==1:
                    view_pro(u)
                elif c==2:
                    add_mny(u)
                elif c==3:
                    with_mny(u)
                elif c==4:
                    statement(u)
                

    elif c==3:
        break
    else:
        print('invalid choice')