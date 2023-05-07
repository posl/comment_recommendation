def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    while True:
        flag = False
        for i in range(n):
            if h[i] > 0:
                flag = True
                break
        if flag == False:
            break
        ans += 1
        for j in range(i, n):
            if h[j] > 0:
                h[j] -= 1
            else:
                break
    print(ans)
