def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    # get lexicographically order
    def get_order(P):
        order = 0
        for i in range(N):
            count = 0
            for j in range(i + 1, N):
                if P[i] > P[j]:
                    count += 1
            order += count * math.factorial(N - i - 1)
        return order
    print(abs(get_order(P) - get_order(Q)))
import math
main()

if __name__ == '__main__':
    main()