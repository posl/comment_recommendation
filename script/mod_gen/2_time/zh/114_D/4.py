def problem114_d():
    N = int(input())
    a = 0
    for i in range(1,N+1):
        if N % i == 0:
            a += 1
    print(a)

if __name__ == '__main__':
    problem114_d()