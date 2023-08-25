# names=['samarth','aditya','aadinath','pritesh','pratiksha']
# names=list('samarth','aditya','aadinath','pritesh','pratiksha')

# for name in names:
#     print(f'hello {name}')

nums=list(range(1,11))
print(nums)

def addNumsInList(li):

    total=0
    for num in li:
        total=total+num
    return total

print(addNumsInList(nums))