def main():
    n = int(input())
    s = [input() for _ in range(n)]
    s_set = set(s)
    for i in range(n):
        if s[i][0] == '!':
            if s[i][1:] in s_set:
                print
