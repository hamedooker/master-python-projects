def end_zeros(num: int) -> int:
    # your code here
    temp_num = num
    cnt = 0
   
    while int(temp_num % 10) == 0:
        temp_num = int(temp_num / 10)
        cnt = cnt + 1
        if int(temp_num / 10) == 0:
            break
    return cnt


if __name__ == "__main__":
    print("Example:")
    print(end_zeros(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")