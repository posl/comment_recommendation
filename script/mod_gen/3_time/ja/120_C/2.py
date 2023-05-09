def main():
    S = input()
    R = S.count('0')
    B = S.count('1')
    print(min(R, B) * 2)

if __name__ == '__main__':
    main()