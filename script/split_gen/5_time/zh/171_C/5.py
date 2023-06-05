def get_name(num):
    if num <= 26:
        return chr(96+num)
    else:
        return get_name((num-1)//26) + get_name(num%26)
