def solve():
    q = int(input())
    s = []
    for i in range(q):
        query = input()
        if query[0] == '1':
            s.append(int(query[2:]))
        elif query[0] == '2':
            x, c = map(int, query[2:].split())
            for j in range(min(c, s.count(x))):
                s.remove(x)
        else:
            print(max(s) - min(s))

if __name__ == '__main__':
    solve()