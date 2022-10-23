#To display text in colour

text = input('Text: ')
while True:
    color = input('Color:')        
    if color == 'red':
      print('\033[31m',text, '\033[31m')
    if color == 'green':
      print('\033[32m',text, '\033[34m')
    if color == 'yellow':
      print('\033[33m',text,'\033[35m') 
    if color == 'blue':
      print('\033[34m',text,'\033[35m')
    if color == 'magenta':
      print('\033[35m',text,'\033[35m')
    else:
      print('Choose a colour please: blue,green,red,yellow,magenta')