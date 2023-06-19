def main():
    N = int(input())
    cnt = 0
    for i in range(1, N+1):
        for j in range(i, N+1):
            for k in range(j, N+1):
                if i*j*k <= N:
                    if i == j and j == k:
                        cnt += 1
                    elif i == j or j == k or i == k:
                        cnt += 3
                    else:
                        cnt += 6
                else:
                    break
    print(cnt)
main()
