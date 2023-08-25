foo="i love mangoos how about mango juice 1234"

# print(foo[::-1])

print(foo.title())
print(foo.islower())
print(foo.isalnum())
print(foo.startswith("i love"))
print(foo.endswith("1234"))
print('*'.join(['My', 'name', 'is', 'Simon']))
print("this is some string".split(' '))
print("     hello     there      ".strip())
print("     hello     there      ".rstrip())
# print(foo[::-1])

# print(r"hello \n there")
# print("love" in foo)
# url="google.com"
# print(url.endswith(".com"))
# names=['amit','rahul','ketaki','shivanya','priyanka','punit']
# print(names)
# newStr="-".join(names)
# print(newStr)
# print(url.split('.')[-1])
# foo1='    jdkaljkldja   '
# print(foo1.strip())

# ext=['jpg','jpeg','png','webp','gif']
# fileName='sdnlad.jpg'
# print("is valid file".center(20,"="))
# print(fileName.split('.')[-1] in ext)

# def isPalindrom(word):
#     if word == word[::-1]:
#         return True
#     else:
#         return False

def isPalindrom2(word): return True if word==word[::-1] else False
print(isPalindrom2("racecar"))


