pharmacy=[]
while True:
    print('''
    1.Add Medicine 
    2.View medicine 
    3.Order Online
    4.Update medicine 
    5.Delete medicine
    6.Search a medicine
    7.Exit''')

    c=int(input('Enter your Choice : '))

    if c==1:
        print('Add Medicine')
        mname=str(input('Enter Medicine: '))
        mname=mname.lower()
        price=float(input('Enter your price : '))
        pharmacy.append({'mname':mname,'price':price})

    elif c==2:
        for i in pharmacy:
            print(i)

    elif c==3:
        for i in pharmacy:
            print(i['mname'])
        print('Type the medicine to buy.')
        prod=input("enter the product : ")
        prod=prod.lower()
        f=0
        for i in pharmacy:
            if i['mname']==prod:
                w=int(input('enter the amount needed..'))
                m=w*i['price']
                print('Total Price=',m)
                print('Thankyou For Shopping...')
                f=1
        if f==0:
            print('not availible')

    elif c==4:
        name=str(input("enter the medicine : "))
        name=name.lower()
        f=0
        for i in pharmacy:
            if i['mname']==name:
                price=float(input('enter the new price : '))
                i['price']=price
                f=1
        if f==0:
            print('invalid number...')

    elif c==5:
        name=str(input("enter the product : "))
        name=name.lower()
        f=0
        for i in pharmacy:
            if i['mname']==name:
                pharmacy.remove(i)
                f=1
        if f==0:
            print('invalid number...')

    elif c==6:
        name=str(input("enter the product : "))
        name=name.lower()
        f=0
        for i in pharmacy:
            if i['mname']==name:
                print('Medicine Name : ',i['mname'])
                print('Medicine Price : ',i['price'])
                f=1
        if f==0:
            print('not availible')

    elif c==7:
        break
    else:
        print('choose Correct option' )