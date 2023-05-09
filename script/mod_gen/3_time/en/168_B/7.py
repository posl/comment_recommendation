def main():
    # Write your code here
    K = int(input())
    S = input()
    if len(S) <= K:
        print(S)
    else:
        print(S[:K] + '...')
main()

if __name__ == '__main__':
    main()