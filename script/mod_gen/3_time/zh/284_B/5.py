def problems284_b():
    T = int(input())
    for i in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        result = 0
        for j in range(N):
            if A[j] % 2 == 1:
                result += 1
        print(result)

if __name__ == '__main__':
    problems284_b()