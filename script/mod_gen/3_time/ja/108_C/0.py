def main():
    N,K = map(int,input().split())
    count = 0
    for a in range(1,N+1):
        for b in range(1,N+1):
            for c in range(1,N+1):
                if a+b+b+c+c+a==3*K:
                    count += 1
    print(count)
main()
