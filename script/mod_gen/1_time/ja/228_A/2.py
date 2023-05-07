def main():
    S, T, X = map(int, input().split())
    if S < T:
        if S <= X < T:
            print("Yes")
        else:
            print("No")
    else:
        if 0 <= X < T or S <= X < 24:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()