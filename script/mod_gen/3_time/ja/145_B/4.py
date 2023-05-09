def main():
    N = int(input())
    S = input()
    if S == S[:N//2]*2:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()