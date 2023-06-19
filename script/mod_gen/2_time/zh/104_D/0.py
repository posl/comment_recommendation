def main():
    S = input()
    Q = S.count("?")
    mod = int(1e9+7)
    count = 0
    for i in range(3**Q):
        T = S
        for j in range(Q):
            T = T.replace("?", "ABC"[i//3**j%3], 1)
        count += T.count("ABC")
    print(count%mod)

if __name__ == '__main__':
    main()