def main():
    S = input()
    if S.count('o') == 4:
        print(4)
    elif S.count('o') == 3:
        print(4 + 4 * S.count('?'))
    elif S.count('o') == 2:
        print(4 + 4 * S.count('?') + 6 * S.count('?') * (S.count('?') - 1) // 2)
    elif S.count('o') == 1:
        print(4 + 4 * S.count('?') + 6 * S.count('?') * (S.count('?') - 1) // 2 + 4 * S.count('?') * (S.count('?') - 1) * (S.count('?') - 2) // 6)
    else:
        print(4 + 4 * S.count('?') + 6 * S.count('?') * (S.count('?') - 1) // 2 + 4 * S.count('?') * (S.count('?') - 1) * (S.count('?') - 2) // 6 + S.count('?') * (S.count('?') - 1) * (S.count('?') - 2) * (S.count('?') - 3) // 24)

if __name__ == '__main__':
    main()