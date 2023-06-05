def mul(a):
    m = 1
    for i in range(len(a)):
        m *= a[i]
    return m
n = int(input())
a = list(map(int, input().split()))

if __name__ == '__main__':
    mul()