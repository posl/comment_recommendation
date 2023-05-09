def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    stone = N
    while stone > 0:
        for i in range(K):
            if stone - A[i] >= 0:
                stone = stone - A[i]
                break
    print(N - stone)
main()
This is my solution. I am not sure if this is the most efficient way to solve this problem, but I would love to know what is wrong with my solution. Thanks in advance!
This is my solution. I am not sure if this is the most efficient way to solve this problem, but I would love to know what is wrong with my solution. Thanks in advance!
It's not wrong, but it's not the most efficient way to solve this problem. You're using brute force, which is not the most efficient way to solve this problem.
I would love to know what is wrong with my solution.
You are not using the fact that A is sorted in ascending order.
You are not using the fact that A is sorted in ascending order.
I am not sure how to use that fact to solve this problem. Could you please explain? Thanks!
I am not sure how to use that fact to solve this problem. Could you please explain? Thanks!
You could use binary search to find the largest A_i that is less than or equal to the number of stones in the pile.
You could use binary search to find the largest A_i that is less than or equal to the number of stones in the pile.
I see. I am not sure how to implement binary search in this problem. Could you please help me with this? Thanks!
I see. I am not sure how to implement binary search in this problem. Could you please help me with this? Thanks!
You could use binary search to find the largest A_i that is less than or equal to the number of stones in the pile.
You could use binary search to find the largest A_i that is less than or equal to the number of stones in the pile.
