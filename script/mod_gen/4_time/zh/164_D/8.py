def main():
    S = input()
    count = 0
    for i in range(len(S)):
        for j in range(i, len(S)):
            if int(S[i:j+1]) % 2019 == 0:
                count += 1
    print(count)

if __name__ == '__main__':
    main()