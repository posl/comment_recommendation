def main():
    S = []
    for i in range(4):
        S.append(input())
    if S.count('H') == 1:
        if S.count('2B') == 1:
            if S.count('3B') == 1:
                if S.count('HR') == 1:
                    print('Yes')
                    return
    print('No')

if __name__ == '__main__':
    main()