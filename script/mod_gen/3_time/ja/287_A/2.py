def main():
    N = int(input())
    S = [input() for _ in range(N)]
    if S.count("For") > N//2:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()