def register():
    print('Register here..')
    if len(usr)==0:
            id='user1000'
    else:
        a=usr[-1]['id']
        b=int(a[4:])
        b+=1
        id='user'+ str(b)
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
        b=int(a[4:])
        b+=1
        id='staff'+ str(b)
    name=str(input('enter staff name : '))
    salary=int(input('enter staff salary : '))
    password=id
    stf.append({'id':id,'name':name,'salary':salary,'password':password})



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
                        3.delete Staff''')
                        c1=int(input('enter your choice : '))
                        if c1==1:
                            add_stf()
        elif f==2:
            print('user login')
        elif f==3:
            print('staff login')
        else:
            print('invalid login')

    elif c==3:
        break
    else:
        print('--Invalid Choice--')