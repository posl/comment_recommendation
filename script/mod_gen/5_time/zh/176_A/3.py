def problems176_a():
    N, X, T = map(int, input().split())
    print((N+X-1)//X*T)

if __name__ == '__main__':
    problems176_a()