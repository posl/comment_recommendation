def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    B = list(map(lambda x: x-1, B))
    max_day = max(A) + max(B)
    day_count = [0] * (max_day + 1)
    for i in range(N):
        day_count[A[i]] += 1
        day_count[A[i]+B[i]+1] -= 1
    for i in range(max_day):
        day_count[i+1] += day_count[i]
    print(*day_count[:-1])
main()

if __name__ == '__main__':
    main()