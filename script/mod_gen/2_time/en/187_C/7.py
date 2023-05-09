def main():
    N = int(input())
    s = [input() for _ in range(N)]
    d = {}
    for i in range(N):
        if s[i][0] == '!':
            s[i] = s[i][1:]
            d[s[i]] = 1
        else:
            d[s[i]] = 0
    for i in range(N):
        if d[s[i]] == 1:
            print(s[i])
            return
    print('satisfiable')
    return

if __name__ == '__main__':
    main()