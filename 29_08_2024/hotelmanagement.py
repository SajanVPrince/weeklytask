htl=[]
import datetime
while True:
    print('''
    1.Add Food Details
    2.View Food
    3.Order Online
    4.Update food
    5.Delete Food details
    6.Search a food
    7.Exit''')

    c=int(input('Enter your Choice : '))

    if c==1:
        print('Add Food')
        fname=str(input('Enter Food: '))
        fname=fname.lower()
        type=str(input('Enter Type : '))
        price=float(input('Enter your price : '))
        htl.append({'fname':fname,'type':type,'price':price})

    elif c==2:
        for i in htl:
            print(i)
    
    elif c==3:
        for i in htl:
            print(i['fname'])
        print('Type the food to buy.')
        prod=input("enter the product : ")
        prod=prod.lower()
        f=0
        for i in htl:
            if i['fname']==prod:
                w=int(input('enter the amount needed..'))
                m=w*i['price']
                print('Total Price=',m)
                print('Thankyou For Shopping...')
                f=1
        if f==0:
            print('not availible')
    
    elif c==4:
        name=str(input("enter the food : "))
        name=name.lower()
        f=0
        for i in htl:
            if i['fname']==name:
                price=float(input('enter the new price : '))
                i['price']=price
                f=1
        if f==0:
            print('invalid number...')
    
    elif c==5:
        name=str(input("enter the product : "))
        name=name.lower()
        f=0
        for i in htl:
            if i['fname']==name:
                htl.remove(i)
                f=1
        if f==0:
            print('invalid number...')
    
    elif c==6:
        name=str(input("enter the product : "))
        name=name.lower()
        f=0
        for i in htl:
            if i['fname']==name:
                print('Food Name : ',i['fname'])
                print('Food Type : ',i['type'])
                print('Food Price',i['price'])
                f=1
        if f==0:
            print('not availible')

    elif c==7:
        break
    else:
        print('choose Correct option' )
