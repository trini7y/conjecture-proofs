import math

print """This is an algorithm to check if the Fermat's theorem is true
i have, The Fermat's last theorem states that no three positive integers a, b, and c 
satisfy the equation a^n + b^n = c^n for any integer value of n greater than 2.
For more on the Fermat's Last Theorem visit ==> https://en.wikipedia.org/wiki/Fermat%27s_Last_Theorem"""
def check_fermat(a, b, c, n):
    first_value = a
    second_value = b
    third_value = c
    power = n
    fermats = math.sqrt((first_value ** power) + (second_value ** power))
    print fermats
    third = math.sqrt(third_value ** power)
    print third
    if fermats == third:
         print "Holy smokes fermats was wrong"
    else:
         print "No that doesn't work"


def input_value():
    print "Input first value" 
    input_a =int(raw_input())
    print "Input second Value: "
    input_b = int(raw_input())
    print "Input third value: "
    input_c =  int(raw_input())
    print "Input power greater than 2: "
    input_power = int(raw_input())
    check_fermat(input_a, input_b, input_c, input_power)
input_value()
