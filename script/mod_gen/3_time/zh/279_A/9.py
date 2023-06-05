def solve():
    s = input()
    count = 0
    for i in range(len(s)):
        if s[i] == 'w':
            for j in range(i+1, len(s)):
                if s[j] == 'w':
                    count += 1
    print(count)

if __name__ == '__main__':
    solve()