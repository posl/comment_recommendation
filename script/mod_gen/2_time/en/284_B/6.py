def odd_count(A):
    count = 0
    for a in A:
        if a%2 == 1:
            count += 1
    return count
T = int(raw_input())
for t in range(T):
    N = int(raw_input())
    A = map(int, raw_input().split())
    print odd_count(A)
