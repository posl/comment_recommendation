def main():
    K = int(input())
    A, B = input().split()
    A_10 = 0
    B_10 = 0
    for i in range(len(A)):
        A_10 += int(A[i]) * K ** (len(A) - 1 - i)
    for i in range(len(B)):
        B_10 += int(B[i]) * K ** (len(B) - 1 - i)
    print(A_10 * B_10)
