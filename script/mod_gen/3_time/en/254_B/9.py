def main():
    n = int(input())
    for i in range(n):
        print(" ".join(map(str, solve(i))))

if __name__ == '__main__':
    main()