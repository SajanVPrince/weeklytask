from data import user,staff
def register():
    if len(user)==0:
        id='abcd1000'
    else:
        a=user[-1]['id']
        b=int(a[4:])
        b+=1
        id=a[:4]+str(b)
    email=str(input('enter your email : '))
    f=0
    for i in user:
        if i['email']==email:
            f=1
            print('email already exists')
            register()
    if f==0:
        name=input('enter your name : ')
        age=int(input('enter your age : '))
        phone=int(input('enter your mobile number : '))
        password=input('enter your password : ')
        acctype='0'
        balance=0
        user.append({'id':id,'name':name,'age':age,'email':email,'phone':phone,'password':password,'acctyp':acctype,'balance':balance,'trans':[]})

def login():
    usr=str(input('enter your user name : '))
    passw=str(input('enter your password : '))
    f=0
    u=''
    if usr=='admin' and passw=='admin':
        f=1
    for i in user:
        if usr==i['email'] and passw==i['password']:
            f=2
            u=i
    return f,u