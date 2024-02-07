# def greet(name,time):
#     print(f'Good {time} {name}. Hope you\'re well')
   
# name = input('enter your name:')
# time = input('enter the time of the day: ')


# greet(name,time)

#function to find area of the circle
def area_of_circle(radius):
    return(3.142*radius*radius)

def volume(area_of_circle, length):
    print (area_of_circle * length)
    

radius = int(input('enter a radius: '))
length = int(input('enter a length: '))


volume(area_of_circle(radius) , length)