def hello(name="user"):
    print(f"Hello {name}, greeting from python")

def add(no1,no2=0):
    return  no1+no2

def fact(num):
    # if we need to find factorial of 5
    # its hould be product of all natural numbers start from 1 till that number
    # 1*2*3*4*5
    total=1
    while(num>0):
        total=total*num
        num=num-1
    return total

def fact2(num):
    total=1
    for n in range(1,num+1):
        total=total*n
    return total



print(fact(5))
print(fact2(5))

# hello("Amit")
# hello()
# print(10-add(23,45))
# print(add(20))