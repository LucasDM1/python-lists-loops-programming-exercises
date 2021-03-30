
my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]

hello=[]
#your code go here:
for i in  range(0, len(my_list)):
    if type(my_list[i]) is dict or type(my_list[i]) is list:
        hello.append(my_list[i])
print(hello)
