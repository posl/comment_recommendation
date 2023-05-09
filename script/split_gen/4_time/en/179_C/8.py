def main():
    N = int(input())
    #N = 1000000
    cnt = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i*j < N:
                cnt += 1
            else:
                break
    print(cnt)
