def main():
    N = int(input())
    S = input()
    T = S[:N//2]
    if N%2 == 0 and S == T + T:
        print("Yes")
    else:
        print("No")
main()
