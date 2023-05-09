def max_absolute_difference():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    return A[-1] - A[0]
print(max_absolute_difference())

if __name__ == '__main__':
    max_absolute_difference()