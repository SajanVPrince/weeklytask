from login_singin import *
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
                1.View Users
                2.Transactions
                3.exit''')
                c=int(input('enter your choice : '))
                if c==1:
                    view_usr()
                elif c==2:
                    transaction()
                elif c==3:
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
                elif c==5:
                    send_mny(u)
                elif c==6:
                    while True:
                        print('''
                            1.Phone
                            2.email
                            3.Age
                            4.Password
                            5.exit''')
                        c1=int(input('enter your choice : '))
                        if c1==1:
                            phone=int(input('enter your phone number : '))
                            u['phone']=phone
                        elif c1==2:
                            email=str(input('enter your email : '))
                            u['email']=email
                        elif c1==3:
                            age=int(input('enter your age : '))
                            u['age']=age
                        elif c1==4:
                            password=str(input('enter your current password : '))
                            if u['password']==password:
                                pass1=str(input('enter your new password : '))
                                u['password']=pass1
                            else:
                                print('Password missmatch...')
                        elif c1==5:
                            break
                        else:
                            print('invalid choice')
                elif c==7:
                    break
                else:
                    print('invalid choice')

# ---------------------------- USER END -----------------------------------         
    elif c==3:
        break
    else:
        print('invalid choice')