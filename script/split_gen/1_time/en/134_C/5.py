def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    max_A = max(A)
    max_A_cnt = A.count(max_A)
    if max_A_cnt == 1:
        for a in A:
            if a == max_A:
                print(max_A)
            else:
                print(max_A)
    else:
        for _ in range(max_A_cnt):
            A.remove(max_A)
        for _ in range(max_A_cnt):
            A.append(max_A)
        for _ in range(max_A_cnt):
            print(max(A))
