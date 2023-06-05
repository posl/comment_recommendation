def is3multi(s):
    sum = 0
    for i in s:
        sum += int(i)
    if sum % 3 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    is3multi()