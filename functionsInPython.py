def hello(name="user"):
    print(f"Hello {name}, greeting from python")

def add(no1,no2=0):
    return  no1+no2
hello("Amit")
hello("Rahul")
print(10-add(23,45))
print(add(20))