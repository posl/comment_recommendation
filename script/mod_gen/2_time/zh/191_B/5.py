def problems191_b():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a = [i for i in a if i != x]
    print(*a)

if __name__ == '__main__':
    problems191_b()