def problem204_b():
    N = int(input())
    A = list(map(int, input().split()))
    print(sum([max(A[i]-10, 0) for i in range(N)]))

if __name__ == '__main__':
    problem204_b()