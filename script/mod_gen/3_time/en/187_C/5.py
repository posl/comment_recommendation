def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    i = 0
    while i < n-1:
        if s[i] == s[i+1]:
            i += 2
        elif s[i] == '!'+s[i+1]:
            print(s[i][1:])
            return
        else:
            i += 1
    print('satisfiable')

if __name__ == '__main__':
    main()