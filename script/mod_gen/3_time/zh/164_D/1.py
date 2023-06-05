def main():
    S = input()
    # print(S)
    count = 0
    for i in range(len(S)):
        for j in range(i + 3, len(S)):
            # print(S[i:j])
            if int(S[i:j]) % 2019 == 0:
                count += 1
    print(count)

if __name__ == '__main__':
    main()