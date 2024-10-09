from login_singin import user
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
    if re.search('^[a-z0-9].*[@ok][a-z]',upi):
        u['balance']+=add
        u['trans'].append({'day':tran.strftime("%x"),'amt':+add,'mode':'Deposit'})
        print('Amount credited to  your account')
    else:
        print('invalid upi id.Please try again')

def with_mny(u):
    sub=int(input('enter amount to withdraw : '))
    tran=datetime.datetime.now()
    if u['balance']>sub:
        u['balance']-=sub
        u['trans'].append({'day':tran.strftime("%x"),'amt':-sub,'mode':'Withdraw'})
        print(f'{sub} amount withdrawed your current balance is {u['balance']}')
    else:
        print('insufficent fund')

def statement(u):
    print('{:<10}{:<10}{:<10}'.format('DATE','AMOUNT','MODE'))
    print('_'*30)
    for i in u['trans']:
        print('{:<10}{:<10}{:<10}'.format(i['day'],i['amt'],i['mode']))
    
def send_mny(u):
    upi=input('enter the upi to be credited: ')
    amt=int(input('enter the amount to transfer : '))
    upi1=input('enter your upi id : ')
    tran=datetime.datetime.now()
    if re.search('^[a-z0-9].*[@ok][a-z]',upi) and  re.search('^[a-z0-9].*[@ok][a-z]',upi1) and u['balance']>amt:
        u['balance']-=amt
        u['trans'].append({'day':tran.strftime("%x"),'amt':-amt,'mode':'Upi'})
        print(f'{amt} amount credited to {upi} and your current balance is {u['balance']}')
    else:
        print('Insufficient amount')

