num = 29

flag = False

for i in range(2,num):
    if(num % i == 0):
        flag = True
        break
if flag:
    print(num,"This is not a prime number")
else:
    print(num,"This is a prime number")