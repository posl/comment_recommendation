def is753(n):
    n_str = str(n)
    return '7' in n_str and '5' in n_str and '3' in n_str and n_str.count('7') + n_str.count('5') + n_str.count('3') == len(n_str)
