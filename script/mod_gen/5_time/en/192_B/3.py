def main():
    S = input()
    S_odd = S[::2]
    S_even = S[1::2]
    if S_odd.islower() and S_even.isupper():
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()