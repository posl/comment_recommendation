def main():
    K = int(input())
    d = 1
    while K >= 2 ** d:
        K -= 2 ** d
        d += 1
    ans = "2" * (d - 1) + "0" * (d - 1 - K) + "2" + "0" * K
    print(ans)

if __name__ == '__main__':
    main()