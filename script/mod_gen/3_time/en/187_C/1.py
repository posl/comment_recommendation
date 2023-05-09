def main():
    n = int(input())
    s = [input() for _ in range(n)]
    s.sort()
    for i in range(n-1):
        if s[i] == s[i+1]:
            print(s[i])
            return
        elif s[i] == s[i+1][1:]:
            print(s[i+1])
            return
    print('satisfiable')

if __name__ == '__main__':
    main()