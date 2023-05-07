def main():
    N = int(input())
    ans = 0
    for i in range(1,int(N**0.5)+1):
        if N//i**3 != 0:
            ans += N//i**3
    print(ans)

if __name__ == '__main__':
    main()