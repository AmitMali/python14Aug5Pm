# myfile=open('sample.txt','r')
# print(myfile.read())
# myfile.close()

# with open('sample.txt') as myfile:
#     op=myfile.read()
#     print(op)

# with open('sample1.txt','a') as file1:
#     file1.write("\nhello world, python file")

name=input("enter name")
email=input("enter email")
contact=input("enter mobile number")
with open('contacts.csv','a') as myfile:
    myfile.write(f'{name},{email},{contact}\n')
