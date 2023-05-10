def main():
    n = int(input())
    s = list(map(int, input().split()))
    a = [0]*n
    a[0] = s[0]
    for i in range(n-1):
        a[i+1] = s[i+1] - a[i]
    print(*a)
