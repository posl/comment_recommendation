def main():
    n = int(input())
    C = list(map(int, input().split()))
    C.sort()
    ans = 1
    for i in range(n):
        ans = ans * (C[i]-i) % 1000000007
    print(ans)
