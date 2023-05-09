def main():
    S, T = map(str, input().split())
    if S < T:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()