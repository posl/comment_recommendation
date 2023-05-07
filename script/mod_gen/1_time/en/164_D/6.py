def main():
    S = input()
    l = len(S)
    count = 0
    for i in range(l):
        for j in range(i, l):
            if int(S[i:j+1]) % 2019 == 0:
                count += 1
    print(count)

if __name__ == '__main__':
    main()