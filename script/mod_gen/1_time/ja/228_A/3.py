def main():
    S, T, X = map(int, input().split())
    if S <= X < T:
        print("Yes")
    elif S > T and (X >= S or X < T):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()