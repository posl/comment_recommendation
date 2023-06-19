def snow(a,b):
    n = b-a
    count = 0
    for i in range(1,n+1):
        count += i
    return count - a

if __name__ == '__main__':
    snow()