def main():
    # Read the input
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # Sort the input
    A.sort(reverse=True)
    # Check if M popular items can be selected
    if A[M-1] >= sum(A) / (4*M):
        print("Yes")
    else:
        print("No")
