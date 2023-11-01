def main():
    n = int(input())
    s = [input() for i in range(n)]
    for i in range(n):
        if s[i][0] == '!':
            s[i] = s[i][1:]
    s.sort()
    for i in range(n-1):
