def main():
    N = int(input())
    words = [input() for _ in range(N)]
    if len(set(words)) == N and all(words[i][0] == words[i - 1][-1] for i in range(1, N)):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()