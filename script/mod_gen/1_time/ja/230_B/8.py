def main():
    S = input()
    T = "oxx" * 10**5
    T = T[:len(S)]
    if S == T:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()