def main():
    n = int(input())
    s = [input() for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if s[i][j] == "#":
                continue
            s[i] = s[i][:j] + "#" + s[i][j+1:]
            if check(s):
                print("Yes")
                return
            s[i] = s[i][:j] + "." + s[i][j+1:]
            for k in range(i, n):
                for l in range(n):
                    if s[k][l] == "#":
                        continue
                    s[k] = s[k][:l] + "#" + s[k][l+1:]
                    if check(s):
                        print("Yes")
                        return
                    s[k] = s[k][:l] + "." + s[k][l+1:]
    print("No")

if __name__ == '__main__':
    main()