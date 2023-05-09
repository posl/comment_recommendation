def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    count = 0
    for i in range(1000):
        if A[0] <= i+1 and i+1 <= B[0]:
            if A[1] <= i+1 and i+1 <= B[1]:
                if A[2] <= i+1 and i+1 <= B[2]:
                    count += 1
    print(count)
