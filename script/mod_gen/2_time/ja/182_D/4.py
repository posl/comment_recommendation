def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = [0]
    for i in range(N):
        B.append(B[i]+A[i])
    print(max(B)-min(B))

if __name__ == '__main__':
    main()