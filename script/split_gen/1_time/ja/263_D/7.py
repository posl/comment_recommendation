def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, L, R)
    #print(A)
    #print(sum(A))
    #print(min(A))
    if L > R:
        L,R = R,L
    if L >= 0:
        print(sum(A) + N*L)
        return
    if R <= 0:
        print(sum(A) + N*R)
        return
    #ここまでで、L,Rは0を含む
    #print(sum(A))
    #print(sum(A) + N*L)
    #print(sum(A) + N*R)
    #print(sum(A) + N*(L+R)//2)
    #print(N*(L+R)//2)
    #ここから、L,Rは0を含む
    #A_i>0の時、A_iをLで置き換える
    #A_i<0の時、A_iをRで置き換える
    #A_i=0の時、A_iをL,Rのうち小さい方で置き換える
    #A_i=0の時、A_iをL,Rのうち大きい方で置き換える
    #A_i>0の時、A_iをLで置き換える
    #A_i<0の時、A_iをRで置き換える
    #A_i=0の時、A_iをL,Rのうち小さい方で置き換える
    #A_i=0の時、A_iをL,Rのうち大きい方で置き換える
    #print(min(A))
    #print(max(A))
    #print(L)
    #print(R)
    #A_i=0の時、A_iをL,Rのうち小さい方で置き換える
    #A_i=0の時、A_iをL,Rのうち大きい方で置き換える
    #print(N)
    #print(L)
    #print(R)
    #print(A)
    #print(sum(A))
    #A_i=0の時、
