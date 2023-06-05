def main():
    N, X = map(int, input().split())
    A_list = []
    B_list = []
    for i in range(N):
        A, B = map(int, input().split())
        A_list.append(A)
        B_list.append(B)
    sum = 0
    for i in range(N):
        sum += A_list[i] * B_list[i]
    if sum <= X:
        print("Yes")
    else:
        print("No")
