def main():
    # Write your code here
    A, B, C = map(int, input().split())
    if A-B >= C:
        print(C)
    else:
        print(A-B)
