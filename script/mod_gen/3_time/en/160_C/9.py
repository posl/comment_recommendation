def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    # The minimum distance to travel is the largest distance between two houses.
    # If we sort the distances in ascending order, the largest distance is the difference between the last and first houses.
    # If the pond is circular, the distance between the first and last houses is K minus the difference between the last and first houses.
    # Therefore, the minimum distance to travel is the maximum of the difference between the last and first houses and K minus the difference between the last and first houses.
    # If there are only two houses, the minimum distance to travel is the difference between the last and first houses.
    if N == 2:
        print(A[1] - A[0])
    else:
        A.append(A[0] + K)
        B = [A[i + 1] - A[i] for i in range(N)]
        print(max(max(B), K - min(B)))

if __name__ == '__main__':
    main()