list = [11,22,33]
len = len(list)
print(f"lenth of list is {len}")
my_list = []
print(my_list)
for x in range(1,len+1):
    obj = {}
    obj['name'] = 'akshay'
    obj['age'] = 24
    my_list.append(obj)

# print(my_list)

for ind , data in enumerate(my_list):
    print(ind , data)
    print(type(ind))