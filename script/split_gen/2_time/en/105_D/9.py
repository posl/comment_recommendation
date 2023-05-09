def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # Initialize the array to store the number of candies in each box
    candies = [0] * (N+1)
    for i in range(N):
        candies[i+1] = candies[i] + A[i]
    # Initialize the array to store the number of boxes with each sum of candies
    box = [0] * M
    for i in range(N+1):
        box[candies[i] % M] += 1
    # Calculate the number of pairs
    ans = 0
    for i in range(M):
        ans += box[i]*(box[i]-1)//2
    # Output
    print(ans)
