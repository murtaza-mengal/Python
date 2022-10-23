
def calculate_lcm(num1,num2):
    l = max(num1, num2)
    temp = l
    s = min(num1, num2)
    y = 0
    while l <= (num1 * num2):
        if l % s == 0:
            lcm = l
            break
        else:
            y += 1
            l = temp * y
    return lcm

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
print('LCM is: ', calculate_lcm(num1,num2))