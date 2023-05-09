def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A_even = []
    A_odd = []
    for i in range(N):
        if i % 2 == 0:
            A_even.append(A[i])
        else:
            A_odd.append(A[i])
    A_odd = [0] + A_odd
    if sum(A_even) + sum(A_odd) <= X:
        print("Yes")
    else:
        print("No")
