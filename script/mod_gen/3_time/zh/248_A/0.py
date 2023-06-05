def find_missing_number(s):
    for i in range(10):
        if str(i) not in s:
            print(i)
            break

if __name__ == '__main__':
    find_missing_number()