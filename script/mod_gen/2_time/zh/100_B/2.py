def problems100_b():
    D, N = map(int, input().split())
    if D == 0:
        print(N if N != 100 else 101)
    elif D == 1:
        print(N * 100 if N != 100 else 10100)
    else:
        print(N * 10000 if N != 100 else 1010000)

if __name__ == '__main__':
    problems100_b()