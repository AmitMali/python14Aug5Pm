# def add(a,b):
#     return a+b

# print(add(20,30))

# add1=lambda a,b :a+b
# print(add1(34,4))

# def isEven(no):
#     if no%2==0:
#         return True
#     else:
#         return False

# print(isEven(33))

# nums=[45,67,43,86,78,44,66,34,31,60,32,23,30]

# evens=filter( isEven,nums)
# print(list(evens))

# evens1=filter(lambda no:no%2==0,nums)
# print(list(evens1))

marks=[45,67,43,86,78,44,66,34,31,60,32,23,30]

# passed=filter(lambda mark:mark>=35,marks)
# print(list(passed))
# print(len(list(passed)))

def grase(mark):
    if mark>=30 and mark<=33:
        return 35
    else:
        return mark

gressPass=map( grase,marks)
print(list(gressPass))
