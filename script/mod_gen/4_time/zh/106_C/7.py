def get_str(s):
    result = ""
    for i in s:
        result += i * int(i)
    return result

if __name__ == '__main__':
    get_str()