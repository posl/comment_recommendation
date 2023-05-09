def main():
    X = int(input())
    ans = 0
    bal = 100
    while bal < X:
        bal = int(bal * 1.01)
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()