def main():
    n = int(input())
    s = input()
    w = list(map(int, input().split()))
    #print(n, s, w)
    s = list(s)
    #print(s)
    #print(w)
    # 二分法
    def func(x):
        res = 0
        for i in range(n):
            if s[i] == '1':
                if w[i] >= x:
                    res += 1
            else:
                if w[i] < x:
                    res += 1
        return res
    l = 0
    r = 10 ** 9 + 1
    while r - l > 1:
        mid = (l + r) // 2
        if func(mid) >= n // 2 + 1:
            l = mid
        else:
            r = mid
    print(l)
