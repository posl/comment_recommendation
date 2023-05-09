def main():
    N = int(input())
    S = input()
    count = 0
    for i in range(N):
        if S[i] == '"':
            count += 1
        elif S[i] == ',':
            if count % 2 == 1:
                print('.', end='')
            else:
                print(',', end='')
        else:
            print(S[i], end='')
    print()

if __name__ == '__main__':
    main()