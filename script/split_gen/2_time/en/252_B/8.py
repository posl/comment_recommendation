def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # Sort A in descending order
    A.sort(reverse=True)
    # Check if the greatest tastiness food is disliked
    if B.count(A.index(B[0])+1) > 0:
        print("Yes")
    else:
        print("No")
