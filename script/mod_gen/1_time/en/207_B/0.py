def main():
    A,B,C,D = map(int,input().split())
    count = 0
    while A > D * C:
        A += B
        C += D
        count += 1
        if count > 100000:
            print(-1)
            return
    print(count)
main()
