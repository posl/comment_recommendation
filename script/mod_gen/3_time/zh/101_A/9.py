def get_result(s):
    result = 0
    for i in s:
        if i == '+':
            result += 1
        else:
            result -= 1
    return result

if __name__ == '__main__':
    get_result()