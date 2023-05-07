def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    W_sorted = sorted(W)
    W_sorted.append(-1)
    ans = 0
    for i in range(N):
        if S[i] == '0' and W_sorted[i] != W_sorted[i+1]:
            ans += 1
        elif S[i] == '1' and W_sorted[i] == W_sorted[i+1]:
            ans += 1
    print(ans)
main()
I am not sure why this is not working. I am getting only 3 points for this problem. Can you please help me with this?
I have tried to solve this problem using binary search. I have sorted the weights and then used binary search to find the correct value of X.
I am not sure why this is not working. I am getting only 3 points for this problem. Can you please help me with this?
I have tried to solve this problem using binary search. I have sorted the weights and then used binary search to find the correct value of X.
I am not sure why this is not working. I am getting only 3 points for this problem. Can you please help me with this?
I have tried to solve this problem using binary search. I have sorted the weights and then used binary search to find the correct value of X.
I am not sure why this is not working. I am getting only 3 points for this problem. Can you please help me with this?
I have tried to solve this problem using binary search. I have sorted the weights and then used binary search to find the correct value of X.
I am not sure why this is not working. I am getting only 3 points for this problem. Can you please help me with this?
I have tried to solve this problem using binary search. I have sorted the weights and then used binary search to find the correct value of X.
I am not sure why this is not working. I am getting only 3 points for this problem. Can you please help me with this?
I have tried to solve this problem using binary search. I have sorted the weights and then used binary search to find the correct value of X.
I am not sure why this is not working. I am getting only 3 points for this problem. Can you please help me with this?
I have tried to solve this problem using binary search. I

if __name__ == '__main__':
    main()