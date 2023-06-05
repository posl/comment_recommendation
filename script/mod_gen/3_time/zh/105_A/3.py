def problem105_a():
    n,k = input().split()
    n = int(n)
    k = int(k)
    if n % k == 0:
        print(0)
    else:
        print(1)

if __name__ == '__main__':
    problem105_a()