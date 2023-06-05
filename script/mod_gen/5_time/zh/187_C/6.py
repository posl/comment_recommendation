def solve():
    n = int(input())
    s = [input() for _ in range(n)]
    s1 = set()
    s2 = set()
    for i in s:
        if i[0] == '!':
            s2.add(i[1:])
        else:
            s1.add(i)
    s = s1 & s2
    if len(s) == 0:
        print('satisfiable')
    else:
        print(s.pop())

if __name__ == '__main__':
    solve()