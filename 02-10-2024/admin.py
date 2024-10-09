from login_singin import user

def view_usr():
    print('user details')
    print('{:<10}{:<10}{:<10}{:<10}'.format('ID','NAME','EMAIL','PHONE'))
    print('_'*50)
    for i in user:
        print('{:<10}{:<10}{:<10}{:<10}'.format(i['id'],i['name'],i['email'],i['phone']))

def transaction():
    print('{:<10}{:<10}{:<10}'.format('DATE','AMOUNT','MODE'))
    print('_'*30)
    for i in user[0]['trans']:
        print('{:<10}{:<10}{:<10}'.format(i['day'],i['amt'],i['mode']))
