def main():
    A, B, C, D = map(int, input().split())
    if A > B * D:
        print(-1)
        return
    if B <= C:
        print(0)
        return
    count = 0
    while A > B * D:
        A += B
        A -= C
        count += 1
    print(count)

if __name__ == '__main__':
    main()