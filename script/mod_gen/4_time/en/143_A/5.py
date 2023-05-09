def main():
    A, B = map(int, input().split())
    ans = max(0, A - 2 * B)
    print(ans)

if __name__ == '__main__':
    main()