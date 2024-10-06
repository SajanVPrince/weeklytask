from data import user
import datetime
import re

def view_pro(u):
    print('My Profile')
    print('{:<10}{:<14}{:<10}{:<20}{:<10}{:<10}'.format('ID','NAME','PHONE','EMAIL','PASSWORD','BALANCE'))
    print('_'*74)
    print('{:<10}{:<14}{:<10}{:<20}{:<10}{:<10}'.format(u['id'],u['name'],u['phone'],u['email'],u['password'],u['balance']))

def add_mny(u):
    add=int(input('enter money to add to your account : '))
    upi=input('enter upi id : ')
    tran=datetime.datetime.now()
    u['trans'].append({'day':tran.strftime("%x"),'amt':add})
    # if re.search('^(a-z).*',upi):
    u['balance']+=add
    print('Amount credited to  your account')
    # else:
    #     print('invalid upi id.Please try again')

def with_mny(u):
    sub=int(input('enter amount to withdraw : '))
    tran=datetime.datetime.now()
    if u['balance']>sub:
        u['balance']-=sub
        u['trans'].append({'day':tran.strftime("%x"),'amt':-sub})
        print(f'{sub} amount withdrawed your current balance is {u['balance']}')
    else:
        print('insufficent fund')

def statement(u):
    print('{:<10}{:<10}'.format('DATE','AMOUNT'))
    print('_'*20)
    for i in u['trans']:
        print('{:<10}{:<10}'.format(i['day'],i['amt']))
