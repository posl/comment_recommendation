def missing_number(s):
    s = list(s)
    for i in range(10):
        if str(i) not in s:
            print(i)
            break

if __name__ == '__main__':
    missing_number()