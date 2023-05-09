def main():
    # input
    K = int(input())
    S = input()
    # compute
    # output
    if len(S) <= K:
        print(S)
    else:
        print(S[:K] + '...')

if __name__ == '__main__':
    main()