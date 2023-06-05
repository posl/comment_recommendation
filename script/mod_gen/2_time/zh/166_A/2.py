def calc(A,B,N):
    max = 0
    for x in range(0, N+1):
        temp = A*x/B - A*(x/B)
        if max < temp:
            max = temp
    return max

if __name__ == '__main__':
    calc()