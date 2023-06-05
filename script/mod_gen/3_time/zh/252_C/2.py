def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    #print(s)
    #print(len(s[0]))
    ans = 0
    for i in range(10):
        flag = 0
        for j in range(n):
            if s[j][i] == '0':
                flag += 1
        if flag == n:
            ans = i+1
            break
    print(ans)

if __name__ == '__main__':
    main()