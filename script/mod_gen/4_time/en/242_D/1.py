def main():
    S = input()
    Q = int(input())
    for i in range(Q):
        t, k = map(int, input().split())
        if t == 0:
            print(S[k - 1])
        else:
            if S[k - 1] == "A":
                print("B")
            elif S[k - 1] == "B":
                print("C")
            else:
                print("A")

if __name__ == '__main__':
    main()