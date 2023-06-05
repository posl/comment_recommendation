def fizzbuzz(n):
    result = 0
    for i in range(1,n+1):
        if i%3 == 0 and i%5 ==0:
            pass
        elif i%3 == 0:
            pass
        elif i%5 == 0:
            pass
        else:
            result += i
    return result

if __name__ == '__main__':
    fizzbuzz()