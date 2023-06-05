def find(n):
    result = 0
    for c in range(1,n):
        if n % c == 0:
            for b in range(c,n):
                if n % b == 0:
                    a = n / b / c
                    if a >= b:
                        break
                    result += 1
    return result

if __name__ == '__main__':
    find()