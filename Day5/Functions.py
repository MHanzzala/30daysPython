items=["Cars","phone",25.5,65.8,"Hammad","Pen","Mouse",135]

str_items=[]
str_num=[]

for i in items:
    if isinstance(i,float) or isinstance(i,int):
        str_num.append(1)
    elif isinstance(i,str):
        str_items.append(i)
    else:
        pass

print(str_items)

print(str_num)

def parse_list(some_list):
    str_list_items = []
    num_list_items = []
    for i in some_list:
        if isinstance(i,float) or isinstance(i,int):
            str_list_items.append(1)
        elif isinstance(i,str):
            num_list_items.append(i)
        else:
            pass
    return num_list_items,str_list_items

print(parse_list(items))