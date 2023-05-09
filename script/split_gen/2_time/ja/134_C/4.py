def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    max_a = max(A)
    max_a_idx = A.index(max_a)
    A.pop(max_a_idx)
    max_a2 = max(A)
    for i in range(N):
        if i == max_a_idx:
            print(max_a2)
        else:
            print(max_a)
