def problems278_a():
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(k):
        a.pop(0)
        a.append(0)
    print(' '.join(map(str, a)))

if __name__ == '__main__':
    problems278_a()