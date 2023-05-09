def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if N == 1:
        print(A[0] + K)
        return
    if N == 2:
        print(max(A[0] + K, A[1] + K, A[1] ^ A[0] + K))
        return
    # N >= 3
    max_A = A[-1]
    min_A = A[0]
    max_A_xor_min_A = max_A ^ min_A
    if max_A_xor_min_A <= K:
        # 1. max_A + K
        # 2. min_A + K
        # 3. max_A_xor_min_A + K
        print(max_A + K)
        return
    # 1. max_A + K
    # 2. min_A + K
    # 3. max_A_xor_min_A + K
    # 4. max_A_xor_min_A + K - 1
    # 5. max_A_xor_min_A + K - 2
    # ...
    # 6. max_A_xor_min_A
    # 7. max_A_xor_min_A - 1
    # 8. max_A_xor_min_A - 2
    # ...
    # 9. 0
    # 10. 1
    # 11. 2
    # ...
    # 12. max_A_xor_min_A - (K - 1)
    # 13. max_A_xor_min_A - K
    # 14. max_A_xor_min_A - (K + 1)
    # ...
    # 15. max_A_xor_min_A - (max_A_xor_min_A - 1)
    # 16. max_A_xor_min_A - max_A_xor_min_A
    # 17. max_A_xor_min_A - (max_A_xor_min_A + 1)
    # ...
    # 18. max_A_xor_min_A - (2 * max_A_xor_min_A - 1)
    # 19. max_A_xor_min_A - (2 * max_A_xor_min_A)
    # 20. max_A_xor_min_A - (2 * max_A_xor_min_A + 1)
    # ...
    # 21. max

if __name__ == '__main__':
    main()