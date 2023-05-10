def main():
    N = int(input())
    ans = 1000 - N % 1000
    if ans == 1000:
        ans = 0
    print(ans)

if __name__ == '__main__':
    main()