import time
from random import randint

for i in range(1,85):
    print('')

space=""
for i in range(1,1000):
    count=randint(1,100)
    while(count>0):
        space+=' '
        count-=1

    if(i%10==0):
        print(space+'happy new year ')
    elif(i%9==0):
        print(space+"wow")
    elif (i % 8 == 0):
        print(space + "ywaah")
    elif (i % 7 == 0):
        print(space + "hayeee")
    elif (i % 6 == 0):
        print(space + "wowww")
    else:
        print(space+"tadaaa")
    space=''
    time.sleep(0.2)

