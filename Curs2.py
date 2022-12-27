def print_info(x):
    print(x)
    x_type=type(x)
    print(x_type)

name='Tampi'
age=5
is_cat=True
kg=5.7
list=[name,age,is_cat,kg]
for i in list:
    print_info(i)