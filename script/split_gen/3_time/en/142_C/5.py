def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    order = [0]*N
    for i in range(N):
        order[A[i]-1] = i+1
    print(*order)
