def main():
    N = int(input())
    cnt = 0
    for a in range(1, N+1):
        for b in range(1, N+1):
            if a * b + b >= N:
                break
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()