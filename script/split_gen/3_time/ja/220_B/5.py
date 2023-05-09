def main():
    K = int(input())
    A,B = map(int, input().split())
    #print(A,B)
    #print(K)
    A10 = 0
    B10 = 0
    for i in range(len(str(A))):
        A10 += int(str(A)[i]) * (K ** (len(str(A)) - i - 1))
    for j in range(len(str(B))):
        B10 += int(str(B)[j]) * (K ** (len(str(B)) - j - 1))
    print(A10 * B10)
