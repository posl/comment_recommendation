def main():
    S = input()
    K = int(input())
    S = S.replace('.', ' ')
    S = S.split()
    if len(S) == 1:
        print(len(S[0]))
    elif len(S) == 0:
        print(0)
    else:
        count = 0
        for i in range(len(S)):
            count += len(S[i])
        count += K - 1
        print(count)

if __name__ == '__main__':
    main()