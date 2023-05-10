def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = [0]
    for i in range(n):
        s.append(s[i] + a[i])
    #print(s)
    max_p = 0
    max_s = 0
    for i in range(n+1):
        if s[i] > max_s:
            max_s = s[i]
        if max_p < max_s:
            max_p = max_s
    print(max_p)
