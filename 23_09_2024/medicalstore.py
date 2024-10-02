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
        usr.append({'email':email,'name':name,'id':id,'phone':phone,'location':location,'pin':pin,'password':password,'orders':[]})

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
    for i in stf:
        if user==i['id'] and passw==i['password']:
            f=3
            s=i
    return f,u,s

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

def view_spro(s):
    print('Staff details')
    print('{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format('ID','NAME','SALARY','PHONE','LOCATION','EMAIL','PASSWORD'))
    print('_'*70)
    print('{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format(s['id'],s['name'],s['salary'],s['phone'],s['location'],s['email'],s['password']))

def add_med():
    if len(med)==0:
            id='med1000'
    else:
        a=med[-1]['id']
        b=int(a[3:])
        b+=1
        id= a[:3]+ str(b)
    name=str(input('enter the name of medicine : '))
    price=int(input('enter the price : '))
    stock=int(input('enter the stock : '))
    med.append({'id':id,'name':name,'price':price,'stock':stock})

def price_cng():
    id=str(input('enter id : '))
    f=0
    for i in med:
        if i['id']==id:
            price=int(input('enter new price : '))
            i['price']=price
            f=1
            print('price updated')
    if f==0:
        print('no id availible')

def stock_cng():
    id=str(input('enter id : '))
    f=0
    for i in med:
        if i['id']==id:
            stock=int(input('enter new stock : '))
            i['stock']=stock
            f=1
            print('stock updated')
    if f==0:
        print('no id availible')

def delete_med():
    id=str(input('enter id : '))
    f=0
    for i in med:
        if i['id']==id:
            med.remove(i)
            print('data deleted')
            f=1
    if f==0:
        print('no id availible')

def buy_prod(u):
    print('Medicine list')
    print('{:<10}{:<10}{:<10}'.format('ID','NAME','PRICE'))
    print('_'*30)
    for i in med:
        print('{:<10}{:<10}{:<10}'.format(i['id'],i['name'],i['price']))
    buy=str(input('enter product id : '))
    f=0
    # for i in med:
    if i['id']==buy:
        if i['stock']>0:
            i['stock']-=1
            # ---------------
            u['orders'].append(buy)
            # ---------------
            f=1
            amt=int(input('enter the amount needed : '))
            ttl=i['price']*amt
            print('Total Bill amount is : ',ttl)
        else:
            print('out of stock')   
    if f==0:
        print('no id availible')

def view_orders():
    print('{:<10}{:<10}{:<10}'.format('ID','NAME','ORDERS'))
    print('_'*30)
    for i in usr:
        print('{:<10}{:<10}{:<10}'.format(i['id'],i['name'],i['orders']))
    
def v_uodr(u):
    print('{:<10}'.format('ORDERS'))
    print('_'*10)
    print('{:<10}'.format(u['orders']))
    
        

usr=[{'id': 'user1000', 'name': 'a', 'email': 's@', 'phone': 2, 'location': 'd', 'pin': 2, 'password': 'asdf','orders':[]}]
stf=[{'id': 'staff1000', 'name': 'sa', 'salary': 2, 'password': 'asdf', 'phone': 99, 'location': 'd', 'email': 'sa@'}]
med=[{'id': 'med1000', 'name': 'para', 'price': 200, 'stock': 2}]
while True:
    print('''
    1.Register as user
    2.Login
    3.exit''')
    c=int(input('enter your choice : '))
    if c==1:
        register()
    elif c==2:
        f,u,s=login()

        # Admin Login

        if f==1:
            while True:
                print('''
                1.Staffs
                2.View Users
                3.View Medicines
                4.View Staffs
                5.View Orders
                6.exit''')
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
                    view_orders()
                elif c==6:
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
                4.Buy product
                5.View Orders
                6.exit''')
                c=int(input('enter your choice : '))
                if c==1:
                    view_pro(u)
                elif c==2:
                    for i in med:
                        print(i)
                elif c==3:
                    while True:
                        print('''
                        1.Update Name
                        2.Update Phone
                        3.Update email
                        4.Update Location
                        5.Update Pin
                        6.Update Password 
                        7.exit''')
                        c1=int(input('enter your choice : '))
                        if c1==1:
                            name=str(input('enter your name : '))
                            u['name']=name
                        elif c1==2:
                            phone=int(input('enter your number : '))
                            u['phone']=phone
                        elif c1==3:
                            email=str(input('enter your mail : '))
                            u['email']=email
                        elif c1==4:
                            location=str(input('enter your location : '))
                            u['location']=location
                        elif c1==5:
                            pin=int(input('enter your pin : '))
                            u['pin']=pin
                        elif c1==6:
                            password=str(input('enter your new password : '))
                            u['password']=password
                        elif c1==7:
                            break
                        else:
                            print('invalid choice')
                elif c==4:
                    buy_prod(u)
                elif c==5:
                    v_uodr(u)
                elif c==6:
                    break
                else:
                    print('invalid choice')

        # staff login

        elif f==3:
            if s['id']==s['password']:
                    phone=int(input('enter your number : '))
                    location=str(input('enter your location : '))
                    email=str(input('enter your email : '))
                    password=str(input('enter a new password : '))
                    s['phone']=phone
                    s['location']=location
                    s['email']=email
                    s['password']=password
            while True:
                print('''
                1.View profile
                2.Add Medicines
                3.Update Medicines
                4.Delete Medicines
                5.Update profile
                6.View Orders
                7.exit''')
                c=int(input('enter your choice : '))
                if c==1:
                    view_spro(s)
                elif c==2:
                    add_med()
                elif c==3:
                    while True:
                        print('''
                        1.Price
                        2.Stock
                        3.exit''')
                        c1=int(input('enter the choice : '))
                        if c1==1:
                            price_cng()
                        elif  c1==2:
                            stock_cng()
                        elif c1==3:
                            break
                        else:
                            print('invalid choice')
                elif c==4:
                    delete_med()
                elif c==5:
                    while True:
                        print('''
                        1.phone
                        2.name
                        3.location
                        4.password
                        5.email
                        6.exit''')
                        c2=int(input('enter your choice : '))
                        if c2==1:
                            phone=int(input('enter your phone number : '))
                            s['phone']=phone
                        elif c2==2:
                            name=str(input('enter your name : '))
                            s['name']=name
                        elif c2==3:
                            location=str(input('enter your location : '))
                            s['location']=location
                        elif c2==4:
                            password=str(input('enter your new password : '))
                            s['password']=password
                        elif c2==5:
                            email=str(input('enter your email : '))
                            s['email']=email
                        elif c2==6:
                            break
                        else:
                            print('invalid choice')
                elif c==6:
                    view_orders()
                elif c==7:
                    break
                else:
                    print('invalid choice')   
        else:
            print('invalid login')
    elif c==3:
        break
    else:
        print('--Invalid Choice--')