def solve():
    #n = int(input())
    #s = [input() for _ in range(n)]
    n = 6
    s = ['a', '!a', 'b', '!c', 'd', '!d']
    #n = 10
    #s = ['red', 'red', 'red', '!orange', 'yellow', '!blue', 'cyan', '!green', 'brown', '!gray']
    a = set()
    for i in range(n):
        if s[i][0] == '!':
            a.add(s[i][1:])
        else:
            a.add('!' + s[i])
    for i in range(n):
        if s[i] in a:
            print(s[i])
            break
    else:
        print('satisfiable')

if __name__ == '__main__':
    solve()