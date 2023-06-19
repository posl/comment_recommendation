def main():
    S = []
    for i in range(10):
        S.append(input())
    for i in range(10):
        if "#" in S[i]:
            A = i+1
            break
    for i in range(10):
        if "#" in S[9-i]:
            B = 10-i
            break
    for i in range(10):
        if "#" in [s[i] for s in S]:
            C = i+1
            break
    for i in range(10):
        if "#" in [s[9-i] for s in S]:
            D = 10-i
            break
    print(A,B)
    print(C,D)

if __name__ == '__main__':
    main()