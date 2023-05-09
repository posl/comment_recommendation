def main():
    S = []
    for i in range(10):
        S.append(input())
    for i in range(10):
        if '#' in S[i]:
            a = i
            break
    for i in range(9, -1, -1):
        if '#' in S[i]:
            b = i
            break
    for i in range(10):
        if '#' in S[i]:
            c = S[i].index('#')
            break
    for i in range(9, -1, -1):
        if '#' in S[i]:
            d = S[i].rindex('#')
            break
    print(a + 1, b + 1)
    print(c + 1, d + 1)

if __name__ == '__main__':
    main()