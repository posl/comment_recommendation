def main():
    H,A = map(int,input().split())
    res = 0
    while H > 0:
        H -= A
        res += 1
    print(res)

if __name__ == '__main__':
    main()