def solve():
    s = input()
    count = 0
    max = 0
    for i in range(3):
        if s[i] == 'R':
            count += 1
        else:
            count = 0
        if max < count:
            max = count
    print(max)

if __name__ == '__main__':
    solve()