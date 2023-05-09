def main():
    ans = 0
    for i in range(9):
        S = input()
        for j in range(9):
            if S[j] == '#':
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()