def main():
    # Read the input
    L, R = map(int, input().split())
    S = input()
    # Reverse the substring
    S = S[:L - 1] + S[L - 1:R][::-1] + S[R:]
    # Print the result
    print(S)

if __name__ == '__main__':
    main()