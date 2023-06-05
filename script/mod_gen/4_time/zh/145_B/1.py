def main():
    N = int(input())
    S = input()
    if N % 2 != 0:
        print('No')
    else:
        half = int(N/2)
        if S[:half] == S[half:]:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()