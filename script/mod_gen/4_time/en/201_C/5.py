def main():
    s = input()
    ans = 0
    for i in range(10 ** 4):
        i = str(i).zfill(4)
        flag = True
        for j in range(4):
            if s[int(i[j])] == 'x':
                flag = False
                break
            elif s[int(i[j])] == '?':
                continue
        if flag:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()