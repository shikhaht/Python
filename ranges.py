# for n in range(5):
#     print(n)


# for n in range(3,10):
#     print(n)

for n in range(0,20,4):
    print(n)

burgers = ['beef', 'chicken','fish', 'tofu', 'shrimp', 'lobster']

# for n in range(len(burgers)):
#     print("Today's burger is: ", burgers[n])

for n in range(len(burgers)-1,-1,-1):
    print(n,burgers[n])