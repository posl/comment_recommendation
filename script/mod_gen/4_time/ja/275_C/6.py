def solve():
    count = 0
    for i in range(9):
        s = input()
        count += s.count("#")
    print(count)

if __name__ == '__main__':
    solve()