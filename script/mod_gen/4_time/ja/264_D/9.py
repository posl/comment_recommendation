def main():
    S = input()
    S = list(S)
    atcoder = list("atcoder")
    count = 0
    for i in range(0,len(S)):
        if i < len(atcoder):
            if S[i] != atcoder[i]:
                count += 1
        else:
            count += 1
    print(count)

if __name__ == '__main__':
    main()