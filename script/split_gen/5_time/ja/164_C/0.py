def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    s.append('dummy')
    cnt = 0
    for i in range(n):
        if s[i] != s[i+1]:
            cnt += 1
    print(cnt)
