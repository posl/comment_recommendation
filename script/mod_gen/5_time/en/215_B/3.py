def problems215_b():
    n = int(input())
    k = 0
    while 2**k <= n:
        k += 1
    print(k-1)

if __name__ == '__main__':
    problems215_b()