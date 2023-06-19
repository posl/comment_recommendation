def main():
    H,A = map(int,input().split())
    res = H//A
    if H%A != 0:
        res += 1
    print(res)

if __name__ == '__main__':
    main()