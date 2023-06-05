def main():
    n = int(input())
    A = [int(i) for i in input().split()]
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if A[i] != A[j]:
                count += 1
    print(count)
