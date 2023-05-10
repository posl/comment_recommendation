def main():
    A, B, C, D = map(int, input().split())
    #print(A, B, C, D)
    if A <= B * D:
        print(-1)
        return
    if B * C >= D * A:
        print(0)
        return
    ans = 0
    while A > B * D:
        ans += 1
        A += C
        B += D
    print(ans)

if __name__ == '__main__':
    main()