def main():
    S = input().split()
    T = input().split()
    if S == T:
        print("Yes")
        return
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            for k in range(3):
                if k == i or k == j:
                    continue
                if S[i] == T[0] and S[j] == T[1] and S[k] == T[2]:
                    print("Yes")
                    return
    print("No")
    return

if __name__ == '__main__':
    main()