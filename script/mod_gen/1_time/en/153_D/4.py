def main():
    H = int(input())
    ans = 0
    while H > 0:
        H = H // 2
        ans += 1
    print(2**ans-1)

if __name__ == '__main__':
    main()