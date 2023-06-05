def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s = list(set(s))
    for i in range(len(s)):
        if s[i][0] == '!':
            if s[i][1:] in s:
                print(s[i][1:])
                exit()
        else:
            if '!' + s[i] in s:
                print(s[i])
                exit()
    print('satisfiable')
main()
