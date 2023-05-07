def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    #Aの種類の数を求める
    A_set = set(A)
    #Aの種類の数がKのときのiの個数を求める
    for i in range(1,N+1):
        #Aの種類の数がiのときのAの種類の数を求める
        A_i = A_set.pop()
        #Aの種類の数がiのときのAの種類の数がKのときのiの個数を求める
        count = 0
        for j in range(N):
            if A[j] > A_i:
                count += 1
                if count == i:
                    print(j+1)
                    break
        else:
            print(0)
