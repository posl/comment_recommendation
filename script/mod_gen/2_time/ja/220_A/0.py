def main():
    A, B, C = map(int, input().split())
    ans = -1
    for i in range(A, B + 1):
        if i % C == 0:
            ans = i
            break
    print(ans)

if __name__ == '__main__':
    main()