def main():
    N = int(input())
    ans = 'No'
    cnt = 0
    for i in range(N):
        D1, D2 = map(int, input().split())
        if D1 == D2:
            cnt += 1
        else:
            cnt = 0
        if cnt >= 3:
            ans = 'Yes'
            break
    print(ans)
