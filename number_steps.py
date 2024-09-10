from time import sleep
n=1
count=0
while n<10000:
    n=n*2
    count = count+1
    print(n,"steps:",count)
    sleep(0.5)