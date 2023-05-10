def main():
    N = int(input())
    cnt = 0
    for i in range(1,N):
        if N % i == 0:
            if (N // i) % 2 == 1:
                cnt += 1
    print(cnt*2)
main()
