def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i in range(n):
        ans.append(a[i] + a[(i+1)%n])
    print(" ".join(map(str, ans)))
