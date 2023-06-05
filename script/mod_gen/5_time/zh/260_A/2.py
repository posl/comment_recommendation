def solve(string):
    for i in string:
        if string.count(i) == 1:
            return i
    return -1

if __name__ == '__main__':
    solve()