def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = set(A)
    C = {}
    for i in B:
        C[i] = A.count(i)
    count = 0
    for i in C.values():
        if i % 2 == 1:
            count += 1
    print(count)
