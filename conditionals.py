
no1=int(input("Enter Number one"))
no2=int(input("Enter Number two"))
no3=int(input("Enter Number three"))

# print(type(no1))
# print(no1+no2)
if no1==no2 and no1==no3:
    print("All numbers are equal")
elif no1>no2 and no1>no3:
    print(f"{no1} is greater")
elif no2>no1 and no2>no3:
    print(f"{no2} is greater")
else:
    print(f"{no3} is greater")
