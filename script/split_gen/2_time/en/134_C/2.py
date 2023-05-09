def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    max1 = max(A)
    max2 = max([a for a in A if a != max1])
    for a in A:
        if a == max1:
            print(max2)
        else:
            print(max1)
