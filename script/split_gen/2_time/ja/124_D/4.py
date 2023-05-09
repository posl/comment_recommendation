def main():
    n, k = map(int, input().split())
    s = input()
    
    ans = 0
    for i in range(n):
        if s[i] == "1":
            continue
        cnt = 0
        for j in range(i, n):
            if s[j] == "0":
                cnt += 1
            else:
                break
        ans = max(ans, cnt)
    
    print(min(n, ans + 2 * k))
