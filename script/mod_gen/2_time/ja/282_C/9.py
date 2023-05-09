def main():
    N = int(input())
    S = input()
    if N == 1:
        print(S)
    else:
        for i in range(N):
            if i % 2 == 1 and S[i] == ',':
                print('.',end='')
            else:
                print(S[i],end='')
        print()

if __name__ == '__main__':
    main()