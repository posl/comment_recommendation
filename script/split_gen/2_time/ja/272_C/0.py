def main():
    N = int(input())
    A = list(map(int, input().split()))
    A_even = [a for a in A if a % 2 == 0]
    if len(A_even) == 0:
        print(-1)
    else:
        print(max(A_even))
