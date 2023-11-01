def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s = sorted(s)
    #print(s)
    max = 0
    for i in range(n):
        cnt = 0
        for j in range(i, n):
            if s[i] == s[j]:
                cnt += 1
