def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    max_a = max(A)
    max_a_count = A.count(max_a)
    if max_a_count > 1:
        print(*[max_a for _ in range(N)])
        return
    max_a_index = A.index(max_a)
    A[max_a_index] = 0
    max_a2 = max(A)
    print(*[max_a2 for _ in range(N)])
main()
