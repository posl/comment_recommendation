def main():
    S = input().split()
    T = input().split()
    for i in range(3):
        for j in range(i+1,3):
            if S[i] == T[i] and S[j] == T[j]:
                print("Yes")
                return
    print("No")

if __name__ == '__main__':
    main()