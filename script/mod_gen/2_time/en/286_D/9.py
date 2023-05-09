def check_if_possible(N,X,A,B):
    coins = []
    for i in range(N):
        for j in range(B[i]):
            coins.append(A[i])
    coins.sort()
    coins.reverse()
    sum = 0
    for i in range(len(coins)):
        sum += coins[i]
        if sum >= X:
            return "Yes"
    return "No"

if __name__ == '__main__':
    check_if_possible()