def main():
    n = int(input())
    ans = 0
    for p in range(2, 10**6):
        if p**3 > n:
            break
        for q in range(p+1, 10**6):
            if p * q**3 > n:
                break
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()