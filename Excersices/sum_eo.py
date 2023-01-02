def sum_eo(num, param_str):
    """ 
    """
    sum = 0
    if (param_str== 'e') :
        temp_num = num-2 if num % 2 == 0 else num-1

        while temp_num > 0:
            sum += temp_num
            temp_num = temp_num - 2
    else:
        while temp_num > 0:
            sum += temp_num
            temp_num = temp_num - 2

    return sum

print(sum_eo(10,'e'))
        