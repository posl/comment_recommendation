def main():
    K = int(input())
    S = input()
    if len(S) > K:
        print(S[:K] + "...")
    else:
        print(S)
main()

if __name__ == '__main__':
    main()