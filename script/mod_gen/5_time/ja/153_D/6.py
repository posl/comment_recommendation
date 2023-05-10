def main():
    H = int(input())
    cnt = 0
    while H > 0:
        cnt += 1
        H = H // 2
    print(2**cnt-1)

if __name__ == '__main__':
    main()