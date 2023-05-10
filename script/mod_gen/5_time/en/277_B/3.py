def main():
    N = int(input())
    S = [input() for _ in range(N)]
    if len(S) == len(set(S)):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()