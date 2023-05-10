def missing_num(s):
    for i in range(10):
        if str(i) not in s:
            return i

if __name__ == '__main__':
    missing_num()