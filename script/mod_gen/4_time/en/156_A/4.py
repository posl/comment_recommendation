def problems156_a():
    N,R = map(int,input().split())
    if N >= 10:
        print(R)
    else:
        print(R + 100 * (10 - N))

if __name__ == '__main__':
    problems156_a()