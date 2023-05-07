def main():
    S = input()
    T = input()
    # Check if the number of distinct characters in S and T are the same
    if len(set(S)) == len(set(T)):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()