def main():
    s = input()
    ans = 0
    for x in range(10000):
        x = str(x).zfill(4)
        for i in range(10):
            if s[i] == 'o' and str(i) not in x:
                break
            if s[i] == 'x' and str(i) in x:
                break
        else:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()