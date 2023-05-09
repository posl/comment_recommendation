def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a + 1 for a in A]
    A.sort(reverse=True)
    print(sum(A[:M]))
