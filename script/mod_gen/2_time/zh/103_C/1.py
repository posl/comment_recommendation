def f(m, a_list):
    result = 0
    for a in a_list:
        result += m % a
    return result

if __name__ == '__main__':
    f()