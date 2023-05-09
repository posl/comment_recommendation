def main():
    N = int(input())
    S = input()
    T = ""
    for i in range(0, N//2):
        T += S[i]
    if S == T*2:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()