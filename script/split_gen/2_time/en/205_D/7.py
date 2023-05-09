def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    k = [int(input()) for _ in range(q)]
    def f(num):
        for i in range(n):
            if num <= a[i]:
                return num
            num += 1
        return num
    for i in range(q):
        print(f(k[i]))
