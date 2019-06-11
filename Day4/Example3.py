list_d=["ALi","Babar","Hammad","Food",321,"Car",456]
list_e=[]
for i in list_d:
    if isinstance(i,int):
        list_e.append(i)
print (list_e)

x=0
for item in list_d:
    print(list_d[x])
    x +=1  # x = x + 1 