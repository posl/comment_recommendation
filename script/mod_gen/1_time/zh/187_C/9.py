def problem187_c():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        if s[i][0] == "!":
            s[i] = s[i][1:]
    s.sort()
    for i in range

if __name__ == '__main__':
    problem187_c()