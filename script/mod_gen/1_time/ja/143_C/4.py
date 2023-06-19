def main():
    n = int(input())
    s = input()
    if n == 1:
        print(1)
        return
    cnt = 1
    for i in range(1, n):
        if s[i-1] != s[i]:
            cnt += 1
    print(cnt)
main()
