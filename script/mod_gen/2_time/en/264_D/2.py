def main():
    S = input()
    atcoder = 'atcoder'
    count = 0
    for i in range(len(S)):
        if S[i] != atcoder[i]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()