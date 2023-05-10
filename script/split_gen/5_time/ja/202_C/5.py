def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [int(i)-1 for i in input().split()]
    count = [0] * n
    for i in range(n):
        count[c[b[i]-1]] += 1
    ans = 0
    for i in range(n):
        ans += count[a[i]-1]
    print(ans)
