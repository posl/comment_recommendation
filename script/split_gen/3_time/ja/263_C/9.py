def main():
    n,m = map(int, input().split())
    a = [0 for i in range(n)]
    def f(i):
        if i==n:
            print(*a)
        else:
            for j in range(1, m+1):
                a[i] = j
                if i==0 or a[i-1] < a[i]:
                    f(i+1)
    f(0)
