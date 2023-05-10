def main():
    H,W,N = map(int,input().split())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    #Aの最小値とBの最小値を求める
    minA = min(A)
    minB = min(B)
    #print(minA)
    #print(minB)
    #AとBをそれぞれminAとminBから引く
    for i in range(N):
        A[i] -= minA
        B[i] -= minB
    #print(A)
    #print(B)
    #AとBの最大値を求める
    maxA = max(A)
    maxB = max(B)
    #print(maxA)
    #print(maxB)
    #AとBをそれぞれmaxAとmaxBから引く
    for i in range(N):
        A[i] -= maxA
        B[i] -= maxB
    #print(A)
    #print(B)
    #AとBの最大値+1を求める
    maxA = max(A)+1
    maxB = max(B)+1
    #print(maxA)
    #print(maxB)
    #AとBの最大値+1をそれぞれ足す
    for i in range(N):
        A[i] += maxA
        B[i] += maxB
    #print(A)
    #print(B)
    #AとBをそれぞれminAとminBに足す
    for i in range(N):
        A[i] += minA
        B[i] += minB
    #print(A)
    #print(B)
    #AとBをそれぞれ1ずつ足す
    for i in range(N):
        A[i] += 1
        B[i] += 1
    #print(A)
    #print(B)
    #AとBの最大値を求める
    maxA = max(A)
    maxB = max(B)
    #print(maxA)
    #print(maxB)
    #カードの

if __name__ == '__main__':
    main()