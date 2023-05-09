def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    a = 0
    b = 0
    for i in range(n):
        a += p[i] * (n-i-1)
        b += q[i] * (n-i-1)
    print(abs(a-b))
