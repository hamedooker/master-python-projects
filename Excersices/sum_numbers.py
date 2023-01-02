from ast import Num
from lib2to3.pytree import convert
import string
from pyparsing import Each


def sum_numbers(num_list_str:str)->int:
    num_list = num_list_str.split(',')
    sum=0
    for num in num_list:
        sum = sum + int(num)

print(sum_numbers('1,2'))


