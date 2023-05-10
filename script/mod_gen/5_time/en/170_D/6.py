def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A_max = A[-1]
    A_count = [0] * (A_max + 1)
    for a in A:
        A_count[a] += 1
    A_count_div = [0] * (A_max + 1)
    for a in A:
        for i in range(2 * a, A_max + 1, a):
            A_count_div[i] += 1
    A_count_div = [N - a - 1 for a in A_count_div]
    ans = sum([a * b for a, b in zip(A_count, A_count_div)])
    print(ans)
    return()

if __name__ == '__main__':
    main()