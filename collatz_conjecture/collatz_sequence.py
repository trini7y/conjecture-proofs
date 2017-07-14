print( '''A program to see if the collatz
conjecture is true \n''')
print ("======****=================*****======= \n")

number = int(input('Input any number: '))
def collazt(number):
  while number > 0:
    if number % 2 == 0:
        number = number // 2
    elif number % 2 == 1:
      number = (3 * number) + 1
    if number == 1:
      print(number)
      break
    print (number)
collazt(number)
    

                                                          
