def find_missing_number(s):
    number = [0,1,2,3,4,5,6,7,8,9]
    for i in s:
        if int(i) in number:
            number.remove(int(i))
    return number[0]

if __name__ == '__main__':
    find_missing_number()