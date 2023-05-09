def main():
    N = int(input())
    A = []
    for _ in range(N):
        A.append(int(input()))
    max_A = max(A)
    max_A_index = A.index(max_A)
    A.pop(max_A_index)
    for i in range(N):
        if i == max_A_index:
            print(max(A))
        else:
            print(max_A)
