def main():
    N = int(input())
    A = list(map(int, input().split()))
    #A = [6, 2, 3]
    #A = [1, 3, 2, 4, 6, 8, 2, 2, 3, 7]
    #A = [2]
    #N = 1
    #N = 10
    #N = 3
    #A = [1, 2, 3]
    #A = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
    #N = 10
    #A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #A = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
    #A = [1, 3, 2, 4, 6, 8, 2, 2, 3, 7]
    #A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    cnt = 0
    #print("A", A)
    for i in range(N):
        for j in range(N):
            for k in range(N):
                #print("i", i, "j", j, "k", k)
                if A[i] == 0 or A[j] == 0:
                    continue
                if A[i] / A[j] == A[k]:
                    #print("A[i]", A[i], "A[j]", A[j], "A[k]", A[k])
                    cnt += 1
    print(cnt)
