from login_singin import *
from data import *
user=[]
while True:
    print('''
    1.Register as new
    2 login
    3.exit''')

    c=int(input('Enter your choice : '))
    if c==1:
        register()

    # elif c==2:
    #     login()