def main():
    N = int(input())
    A = list(map(int,input().split()))
    #Aの中にある数字の数を数える
    count = [0] * (N+1)
    for i in range(N):
        count[A[i]] += 1

if __name__ == '__main__':
    main()