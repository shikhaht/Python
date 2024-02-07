my_name = 'shikha'

def print_name():
    global my_name
    my_name = 'dustin'
    print('the name inside the function is : ', my_name)

print_name()
print('outside the function the name is: ',my_name)