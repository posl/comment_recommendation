def main():
    K = int(input())
    S = str(input())
    if len(S) > K:
        print(S[:K] + "...")
    else:
        print(S)

if __name__ == '__main__':
    main()