def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    A.sort()
    A.append(0)
    ans = 0
    i = 0
    while i < N:
        if A[i] == A[i+1]:
            ans += 1
            i += 2
        else:
            i += 1
    print(ans)
