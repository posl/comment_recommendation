def main():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    total_vote = sum(A)
    if A[m-1] >= total_vote/(4*m):
        print("Yes")
    else:
        print("No")
