import functools
stud1=[45,66,78,56,88,89,65,45]

# total=functools.reduce(lambda total,current:total+current,stud1)
# print(total)

def addEvens(total,current):
    if current%2==0:
        total= total+current
    return total

marks=[45,67,43,86,78,44,66,34,31,60,32,23,30]

marks2=[20,20,20,21,21,21]

total=functools.reduce(addEvens,marks2)
print(total)

