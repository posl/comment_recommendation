def main():
    n = int(input())
    s = input()
    w = list(map(int, input().split()))
    l = 0
    r = 10**9+1
    while r-l > 1:
        m = (r+l)//2
        flag = True
        for i in range(n):
            if s[i] == '0' and w[i] >= m:
                flag = False
                break
        if flag:
            l = m
        else:
            r = m
    print(l)
