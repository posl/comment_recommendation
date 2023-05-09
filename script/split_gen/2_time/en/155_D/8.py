def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [0] + A + [0]
    # print(A)
    l = -10**18
    r = 10**18
    while r - l > 1:
        mid = (l + r) // 2
        # print(l, r, mid)
        cnt = 0
        for i in range(1, N + 1):
            if A[i] >= 0:
                cnt += N - (A[i:].index(0) + i)
                break
            if A[i] * A[i + 1] >= mid:
                cnt += N - (A[i:].index(0) + i)
                continue
            if A[i] * A[-1] < mid:
                continue
            l_ = i + 1
            r_ = N
            while r_ - l_ > 1:
                m_ = (l_ + r_) // 2
                if A[i] * A[m_] >= mid:
                    r_ = m_
                else:
                    l_ = m_
            cnt += N - r_ + 1
        if cnt >= K:
            l = mid
        else:
            r = mid
    print(l)
main()
I'm not sure if this is the correct way to solve this problem. I used binary search to find the K-th number in the sorted list of products of all pairs. I'm not sure if this solution is correct or not. Please let me know if there are any mistakes in my code.
I think this is the correct way to solve this problem. I used binary search to find the K-th number in the sorted list of products of all pairs. I'm not sure if this solution is correct or not. Please let me know if there are any mistakes in my code.
I think this is the correct way to solve this problem. I used binary search to find the K-th number in the sorted list of products of all pairs. I'm not sure if this solution is correct or not. Please let me know if there are any mistakes in my code.
