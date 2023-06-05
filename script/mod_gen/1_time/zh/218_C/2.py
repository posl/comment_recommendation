def main():
    n = int(input())
    s = [input() for i in range(n)]
    t = [input() for i in range(n)]
    for i in range(n):
        for j in range(n):
            if s[i][j] != t[i][j]:
                break
        else:
            continue
        break
    else:
        print("Yes")
        return
    for i in range(n):
        for j in range(n):
            if s[i][j] != t[j][n-i-1]:
                break
        else:
            continue
        break
    else:
        print("Yes")
        return
    for i in range(n):
        for j in range(n):
            if s[i][j] != t[n-i-1][n-j-1]:
                break
        else:
            continue
        break
    else:
        print("Yes")
        return
    for i in range(n):
        for j in range(n):
            if s[i][j] != t[n-j-1][i]:
                break
        else:
            continue
        break
    else:
        print("Yes")
        return
    print("No")
main()
