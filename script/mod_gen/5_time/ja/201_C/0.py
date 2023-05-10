def main():
    s = input()
    ans = 0
    for i in range(10000):
        i = str(i).zfill(4)
        flag = True
        for j in range(10):
            if s[j] == 'o':
                if str(j) not in i:
                    flag = False
            elif s[j] == 'x':
                if str(j) in i:
                    flag = False
        if flag:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()