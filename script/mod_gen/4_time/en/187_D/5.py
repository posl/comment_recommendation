def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    votes = []
    for i in range(N):
        votes.append(2*A[i] + B[i])
    #print(votes)
    votes.sort(reverse=True)
    #print(votes)
    total = sum(votes)
    #print(total)
    count = 0
    for i in range(N):
        count += 1
        total -= votes[i]
        if total < 0:
            break
    print(count)

if __name__ == '__main__':
    main()