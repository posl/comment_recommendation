def main():
    S = input()
    T = input()
    if len(S) != len(T):
        print("No")
        return
    if S == T:
        print("Yes")
        return
    if sorted(S) != sorted(T):
        print("No")
        return
    print("Yes")

if __name__ == '__main__':
    main()