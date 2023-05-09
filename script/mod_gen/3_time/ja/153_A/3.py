def main():
    H, A = map(int, input().split())
    result = 0
    while H > 0:
        result += 1
        H -= A
    print(result)

if __name__ == '__main__':
    main()