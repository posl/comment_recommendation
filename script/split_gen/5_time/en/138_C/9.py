def main():
    n = int(input())
    v = [int(x) for x in input().split()]
    v.sort()
    v = [x/2 for x in v]
    ans = v[0]
    for i in range(1,n):
        ans += v[i]
        ans /= 2
    print(ans)
