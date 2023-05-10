def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0]*(2**n+1)
    for i in range(n):
        ans[a[i]] = 1
    for i in range(1, 2**n+1):
        if ans[i] == 1:
            print(0)
        else:
            j = i
            c = 0
            while j%2 == 0:
                j = j//2
                c += 1
            print(c)
