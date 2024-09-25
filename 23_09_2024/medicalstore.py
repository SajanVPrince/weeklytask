def register():
    print('Register here..')
    if len(usr)==0:
            id='user1000'
    else:
        a=usr[-1]['id']
        b=int(a[4:])
        b+=1
        id=a[:4]+ str(b)
    email=str(input('enter your email : '))
    f=0
    for i in usr:
        if i['email']==email:
            f=1
            print('email already exists..')
            register()
    if f==0:
        name=str(input('enter your name : '))
        phone=int(input('enter your mobile number : '))
        location=str(input('enter your location : '))
        pin=int(input('enter your pincode : '))
        password=str(input('enter your password  : '))
        usr.append({'id':id,'name':name,'email':email,'phone':phone,'location':location,'pin':pin,'password':password})

def login():
    user=str(input('enter your user name : '))
    passw=str(input('enter your password : '))
    f=0
    u=''
    s=''
    if user=='admin' and passw=='admin':
        f=1
    for i in usr:
        if user==i['email'] and passw==i['password']:
            f=2
            u=i
    return f,u

def add_stf():
    print('Add here..')
    if len(stf)==0:
            id='staff1000'
    else:
        a=stf[-1]['id']
        b=int(a[5:])
        b+=1
        id= a[:5]+ str(b)
    name=str(input('enter staff name : '))
    salary=int(input('enter staff salary : '))
    phone=0000000000
    location='xxxxx'
    email='xxxxx'
    password=id
    stf.append({'id':id,'name':name,'salary':salary,'password':password,'phone':phone,'location':location,'email':email})

def salup():
    id=input('enter staff id : ')
    f=0
    for i in stf:
        if i['id']==id:
            salary=int(input('enter updated slary : '))
            i['salary']=salary
            f=1
    if f==0:
        print('invalid id')

def delstf():
    id=input('enter staff id : ')
    f=0
    for i in stf:
        if i['id']==id:
            stf.remove(i)
            f=1
    if f==0:
        print('invalid id')
    
def vusr():
    print('user details')
    print('{:<10},{:<10}{:<10},{:<10},{:<10}'.format('ID','NAME','EMAIL','PHONE','LOCATION'))
    print('_'*50)
    for i in usr:
        print('{:<10}{:<10}{:<10}{:<10}{:<10}'.format(i['id'],i['name'],i['email'],i['phone'],i['location']))

def vstf():
    print('Staff details')
    print('{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format('ID','NAME','SALARY','PHONE','LOCATION','EMAIL'))
    print('_'*60)
    for i in stf:
        print('{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format(i['id'],i['name'],i['salary'],i['phone'],i['location'],i['email']))

def view_pro(u):
    print('My Profile')
    print('{:<10}{:<14}{:<6}{:<10}{:<10}{:<20}{:<10}'.format('ID','NAME','PIN','PHONE','LOCATION','EMAIL','PASSWORD'))
    print('_'*80)
    print('{:<10}{:<14}{:<6}{:<10}{:<10}{:<20}{:<10}'.format(u['id'],u['name'],u['pin'],u['phone'],u['location'],u['email'],u['password']))


usr=[{'id': 'user1000', 'name': 'a', 'email': 's@', 'phone': 2, 'location': 'd', 'pin': 2, 'password': 'asdf'}]
stf=[{'id': 'staff1000', 'name': 'sa', 'salary': 2, 'password': 'staff1000'}]
med=[]
while True:
    print('''
    1.Register as user
    2.Login
    3.exit''')
    c=int(input('enter your choice : '))
    if c==1:
        register()
    elif c==2:
        f,u=login()

        # Admin Login

        if f==1:
            while True:
                print('''
                1.Staffs
                2.View Users
                3.View Medicines
                4.View Staffs''')
                c=int(input('enter your choice : '))
                if c==1:
                    while True:
                        print('''
                        1.Add Staff
                        2.Update Staff salary
                        3.delete Staff
                        4.View Satff
                        5.exit''')
                        c1=int(input('enter your choice : '))
                        if c1==1:
                            add_stf()
                        elif c1==2:
                            salup()
                        elif c1==3:
                            delstf()
                        elif c1==4:
                            for i in stf:
                                print(i)
                        elif c1==5:
                            break
                        else:
                            print('invalid Choice')
                elif c==2:
                    vusr()
                elif c==3:
                    for i in med:
                        print(i)
                elif c==4:
                    vstf()
                elif c==5:
                    break
                else:
                    print('invalid option')
        
        # User Login

        elif f==2:
            while True:
                print('''
                1.View profile
                2.View Medicines
                3.Update profile
                4.buy product
                5.view Orders
                6.exit''')
                c=int(input('enter your choice : '))
                if c==1:
                    view_pro(u)
        elif f==3:
            print('staff login')
        else:
            print('invalid login')

    elif c==3:
        break
    else:
        print('--Invalid Choice--')