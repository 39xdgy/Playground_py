
x_in = input("input the number: ")

x_in = int(x_in)
print(type(x_in))



two_r = x_in % 2
three_r = x_in % 3
five_r = x_in % 5
seven_r = x_in % 7


if(two_r == 0):
    print("two worked")
if(three_r == 0):
    print("three worked")
if(five_r == 0):
    print("five worked")
if(seven_r == 0):
    print("seven worked")
