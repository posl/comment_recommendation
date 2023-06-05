def problem227_a():
    n,k,a = map(int, input().split())
    print((k-1+a-1)%n+1)

if __name__ == '__main__':
    problem227_a()