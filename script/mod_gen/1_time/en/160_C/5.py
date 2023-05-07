def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    diff = [A[i]-A[i-1] for i in range(1, N)]
    diff.append(K-A[N-1]+A[0])
    print(K-max(diff))

if __name__ == '__main__':
    main()