def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    max = 0
    max_s = []
    for i in range(1,n):
        if s[i] == s[i-1]:
            max += 1
            continue
        else:
            if max > 0:
                max_s.append(s[i-1])
            max = 0
    if max > 0:
        max_s.append(s[n-1])
    for i in max_s:
        print(i)
