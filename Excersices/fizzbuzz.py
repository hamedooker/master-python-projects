from ast import Num
import string


def fizzbuzz(num)->string:
    res = ''
    if(num % 5) == 0:
        res = res + 'fizz'
    if(num % 3) == 0:
        res = res + 'buzz'

    return res


print(fizzbuzz(9))
print(fizzbuzz(15))