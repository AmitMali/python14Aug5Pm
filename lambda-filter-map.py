# def add(a,b):
#     return a+b
#
# print(add(2,4))
#
# add1=lambda a,b:a+b
# print(add1(1,3))

nums=list(range(21))

# for x in nums:
#     if x%2==0:
#         print(x)

evens=list(filter(lambda x:x%2==0,nums))
print(evens)

def findOdd(num):
    if num%2!=0:
        return num

odds=list(filter(findOdd,nums))
print(odds)

marks=[45,67,43,86,78,44,66,34,31,60,32,23,30]

passStudents=list(filter(lambda mark:mark>=34,marks))
print(passStudents)


