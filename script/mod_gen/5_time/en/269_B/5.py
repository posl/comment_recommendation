def main():
    S = []
    for i in range(10):
        S.append(input())
    for i in range(10):
        if S[i].find("#") > -1:
            break
    A = i + 1
    for i in range(9, -1, -1):
        if S[i].find("#") > -1:
            break
    B = i + 1
    for i in range(10):
        if S[i].find("#") > -1:
            break
    C = S[i].find("#") + 1
    for i in range(9, -1, -1):
        if S[i].find("#") > -1:
            break
    D = S[i].rfind("#") + 1
    print(A, B)
    print(C, D)
    return

if __name__ == '__main__':
    main()