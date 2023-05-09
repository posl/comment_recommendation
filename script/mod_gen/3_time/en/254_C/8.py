def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, K)
    #print(A)
    #check the difference between the maximum and the minimum
    max_a = max(A)
    min_a = min(A)
    if max_a - min_a > K:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()