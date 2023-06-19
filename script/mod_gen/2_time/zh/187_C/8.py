def main():
    N = int(input())
    s = []
    for i in range(N):
        s.append(input())
    s2 = []
    for i in range(N):
        if s[i][0] == '!':
            s2.append(s[i][1:])
        else:
            s2.append('!' + s[i])
    s2.sort()
    for i in range(N-1):
        if s2[i] == s2[i+1]:
            print(s2[i][1:])
            exit()
    print('satisfiable')

if __name__ == '__main__':
    main()