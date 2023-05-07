def main():
    A,B,C = map(int,input().split())
    ans = 0
    for i in range(100):
        ans += (i+1)*(A/(A+B+C))
        ans += (i+1)*(B/(A+B+C))
        ans += (i+1)*(C/(A+B+C))
        A = A + A
        B = B + B
        C = C + C
    print(ans)

if __name__ == '__main__':
    main()