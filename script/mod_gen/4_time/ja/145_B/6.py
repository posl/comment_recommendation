def main():
    N = int(input())
    S = input()
    if len(S) % 2 == 0:
        if S[:int(len(S)/2)] == S[int(len(S)/2):]:
            print('Yes')
        else:
            print('No')
    else:
        print('No')

if __name__ == '__main__':
    main()