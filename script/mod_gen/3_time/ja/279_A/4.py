def solve():
    s = input()
    count = 0
    for i in range(len(s)):
        if s[i] == "v":
            count += s[i+1:].count("w")
    print(count)

if __name__ == '__main__':
    solve()