def main():
    N = int(input())
    cnt = 0
    for a in range(1, N+1):
        for b in range(a, N+1):
            if a*b > N:
                break
            for c in range(b, N+1):
                if a*b*c <= N:
                    cnt += 1
                else:
                    break
    print(cnt)

if __name__ == '__main__':
    main()