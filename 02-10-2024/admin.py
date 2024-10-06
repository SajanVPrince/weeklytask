from data import user,staff
def add_stf():
    print('Add here..')
    if len(staff)==0:
            id='staff1000'
    else:
        a=staff[-1]['id']
        b=int(a[5:])
        b+=1
        id= a[:5]+ str(b)
    name=str(input('enter staff name : '))
    salary=int(input('enter staff salary : '))
    phone=0000000000
    location='xxxxx'
    email='xxxxx'
    password=id
    staff.append({'id':id,'name':name,'salary':salary,'password':password,'phone':phone,'location':location,'email':email})

def up_sal():
    id=input('enter staff id : ')
    f=0
    for i in staff:
        if i['id']==id:
            salary=int(input('enter updated slary : '))
            i['salary']=salary
            f=1
    if f==0:
        print('invalid id')

def del_stf():
    id=input('enter staff id : ')
    f=0
    for i in staff:
        if i['id']==id:
            staff.remove(i)
            f=1
    if f==0:
        print('invalid id')

def view_staff():
    print('Staff details')
    print('{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format('ID','NAME','SALARY','PHONE','LOCATION','EMAIL'))
    print('_'*60)
    for i in staff:
        print('{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format(i['id'],i['name'],i['salary'],i['phone'],i['location'],i['email']))

def view_usr():
    print('user details')
    print('{:<10},{:<10}{:<10},{:<10},{:<10}'.format('ID','NAME','EMAIL','PHONE','LOCATION'))
    print('_'*50)
    for i in user:
        print('{:<10}{:<10}{:<10}{:<10}{:<10}'.format(i['id'],i['name'],i['email'],i['phone'],i['location']))
