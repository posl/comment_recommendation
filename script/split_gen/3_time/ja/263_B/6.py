def main():
    n = int(input())
    p = [int(i) for i in input().split()]
    ans = 0
    for i in range(1,n):
        if p[i-1] == n:
            ans = i
            break
        else:
            continue
    print(ans)
