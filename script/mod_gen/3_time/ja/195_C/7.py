def main():
    N = int(input())
    ans = 0
    for i in range(1, len(str(N))+1):
        ans += (N//(10**(3*i)))*3
    print(ans)

if __name__ == '__main__':
    main()