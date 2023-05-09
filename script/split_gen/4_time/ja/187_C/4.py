def main():
    n = int(input())
    s = [input() for _ in range(n)]
    t = []
    for i in range(n):
        if s[i][0] == '!':
            t.append(s[i][1:])
        else:
            t.append('!' + s[i])
    t = set(t)
    s = set(s)
    for i in t:
        if i in s:
            print(i)
            exit()
    print('satisfiable')
