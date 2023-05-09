def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        #print(i, N//i, (N//i)*(N//i+1)//2, i*((N//i)*(N//i+1)//2))
        ans += i*((N//i)*(N//i+1)//2)
    print(ans)

if __name__ == '__main__':
    main()