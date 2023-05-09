def main():
    n = int(input())
    s = [input().split() for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and (s[i][0] == s[j][0] or s[i][1] == s[j][1]):
                break
        else:
            print('No')
            break
    else:
        print('Yes')

if __name__ == '__main__':
    main()