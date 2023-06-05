def main():
    N = int(input())
    ans = N
    for i in range(2, int(N**0.5)+1):
        x = i
        while x <= N:
            x *= i
            ans -= 1
    print(ans)
    
main()
