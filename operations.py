name=input("enter name")
email=input("enter email")
contact=input("enter mobile number")
with open(f'{name}{contact}.txt','a') as myfile:
    myfile.write(f'{name},{email},{contact}\n')