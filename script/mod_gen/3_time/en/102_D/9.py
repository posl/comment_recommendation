def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 10**9
    #AをB,C,D,Eに分ける
    #B = A[:i]
    #C = A[i:j]
    #D = A[j:k]
    #E = A[k:]
    #P,Q,R,S = sum(B),sum(C),sum(D),sum(E)
    #max(P,Q,R,S) - min(P,Q,R,S)の最小値
    #Bの最後の要素はどこか
    #Cの最後の要素はどこか
    #Dの最後の要素はどこか
    #Eの最後の要素はどこか
    #Bの最後の要素はCの最初の要素の直前
    #Cの最後の要素はDの最初の要素の直前
    #Dの最後の要素はEの最初の要素の直前
    #i,j,kはそれぞれB,C,Dの最後の要素の直後のインデックス
    #i = 1
    #j = 2
    #k = 3
    #B = A[:i]
    #C = A[i:j]
    #D = A[j:k]
    #E = A[k:]
    #P,Q,R,S = sum(B),sum(C),sum(D),sum(E)
    #print(P,Q,R,S)
    #print(max(P,Q,R,S) - min(P,Q,R,S))
    #i = 1
    #j = 2
    #k = 4
    #B = A[:i]
    #C = A[i:j]
    #D = A[j:k]
    #E = A[k:]
    #P,Q,R,S = sum(B),sum(C),sum(D),sum(E)
    #print(P,Q,R,S)
    #print(max(P,Q,R,S) - min(P,Q,R,S))
    #i = 1
    #j = 3
    #k = 4
    #B = A[:i]
    #C = A[i:j]
    #D = A[j:k]
    #E = A[k:]

if __name__ == '__main__':
    main()