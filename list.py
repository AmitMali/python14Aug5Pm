names=['samarth','aditya','aadinath','pritesh','pratiksha']
# names=list('samarth','aditya','aadinath','pritesh','pratiksha')

# for name in names:
#     print(f'hello {name}')

# nums=list(range(1,11))
# print(nums)
#
# def addNumsInList(li):
#
#     total=0
#     for num in li:
#         total=total+num
#     return total
#
# print(addNumsInList(nums))

print(names[1])
names[1]='ADITYA'
print(names)
names.append("amit")
print(names)
names.insert(1,'ketki')
print(names)
names2=('ganshyam','rahul','amit','uma')
names.extend(names2)
print(names)
names.remove('amit')
print(names)
last=names.pop(3)
print(names,last)
# del names[-2]
# del names    #delete entire list
print(names)
# names.clear()
# print(names)
names.sort(reverse=True)
print(names)
