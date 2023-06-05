def main():
    S = input()
    N = len(S)
    R = S.count('0')
    B = N - R
    print(min(R, B) * 2)

if __name__ == '__main__':
    main()