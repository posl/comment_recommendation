def main():
    n = int(input())
    s = input()
    w = list(map(int, input().split()))
    if s.count('0') == 0 or s.count('1') == 0:
        print(n)
        return
    if s.count('0') == n or s.count('1') == n:
        print(0)
        return
    w.sort()
    for i in range(n):
        if s[i] == '1':
            w[i] = -1
    for i in range(n-1):
        if w[i] == -1:
            continue
        if w[i] < w[i+1]:
            w[i] = -1
    print(w.count(-1))
