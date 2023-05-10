def main():
    N = int(input())
    S = [input() for i in range(N)]
    if N == len(set(S)):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()