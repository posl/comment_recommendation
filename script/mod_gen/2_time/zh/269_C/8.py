def solve():
    for i in range(10):
        s = input()
        if s.find('#') >= 0:
            break
    for j in range(10):
        if s[j] == '#':
            break
    print(i+1,j+1)
    for k in range(10):
        if s[k] != '#':
            break
    print(k+1,j+1)

if __name__ == '__main__':
    solve()