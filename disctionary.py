trainer={
    "name":"amit mali",
    "contact":9595949452,
    "subjects":['python','javascript','c','c++','php'],
    "married":True
}
print(trainer['name'])
print(trainer.get('name'))
print(trainer.keys())
print(trainer.values())
print(trainer.items())
trainer['age']=34
for x,y in trainer.items():
    print(x,y)
    # print(trainer[key])