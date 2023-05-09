def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 1. Sort the array
    A.sort()
    # 2. Calculate the sum of |A_i-A_j| over all pairs i,j such that 1≦ i < j ≦ N
    #    This is done in two steps:
    #    2.1. Calculate the sum of |A_i-A_j| over all pairs i,j such that 1≦ i < j ≦ N/2
    #    2.2. Calculate the sum of |A_i-A_j| over all pairs i,j such that N/2 < i < j ≦ N
    #         and add it to the sum calculated in 2.1
    #    The sum in 2.2 can be calculated by reversing the order of the array
    #    and performing the same calculation as in 2.1
    #    This is done by the function calc_diff
    sum = calc_diff(A[:N//2]) + calc_diff(A[N//2:][::-1])
    # 3. Print the answer
    print(sum)
