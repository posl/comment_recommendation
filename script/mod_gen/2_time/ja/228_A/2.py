def main():
    S, T, X = map(int, input().split())
    if X+0.5 >= S and X+0.5 < T:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()