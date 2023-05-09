def main():
    n, k = map(int, input().split())
    s = input()
    if n == 1:
        print(0)
        return
    if n == 2:
        if s[0] != s[1]:
            print(1)
        else:
            print(0)
        return
    if s[0] == s[-1]:
        count = 0
        for i in range(1, n):
            if s[i] != s[i-1]:
                count += 1
        print(min(n-1, count+2*k))
    else:
        count = 0
        for i in range(1, n):
            if s[i] != s[i-1]:
                count += 1
        print(min(n-1, count+2*k-1))
