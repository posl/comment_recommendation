def main():
    s = input()
    s = s.replace("?", "0")
    ans = 0
    for i in range(10000):
        n = str(i).zfill(4)
        t = s
        for j in range(4):
            t = t.replace("?", n[j], 1)
        if int(t) % 13 == 5:
            ans += 1
    print(ans % (10 ** 9 + 7))

if __name__ == '__main__':
    main()