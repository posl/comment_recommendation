def floor(A,B,N):
    x = 0
    max = 0
    while x <= N:
        if max < A*x/B - A*(x/B):
            max = A*x/B - A*(x/B)
        x += 1
    return max

if __name__ == '__main__':
    floor()