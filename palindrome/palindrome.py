from sys import set_coroutine_origin_tracking_depth

from numpy import true_divide


def isPalindrome(sentence):

    reverse = sentence[::-1]
    return reverse == sentence


sentence = input("Enter a Sentence")


if isPalindrome(sentence):
    print("sentence is Palidrome")

