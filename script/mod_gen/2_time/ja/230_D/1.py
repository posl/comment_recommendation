def main():
    N,D = map(int,input().split())
    L = [0]*N
    R = [0]*N
    for i in range(N):
        L[i],R[i] = map(int,input().split())
    #print(L)
    #print(R)
    ans = 0
    #L[i]からR[i]までの壁がある
    #D個の壁を破壊する
    #破壊するにはD個の壁が連続している必要がある
    #L[i]からR[i]までの壁がある
    #L[i]からL[i]+D-1までの壁がある
    #L[i+1]からL[i+1]+D-1までの壁がある
    #L[i]からL[i]+D-1までの壁とL[i+1]からL[i+1]+D-1までの壁が重なっている
    #L[i]+D-1 < L[i+1] ならば、L[i]からL[i]+D-1までの壁とL[i+1]からL[i+1]+D-1までの壁は重なっていない
    #L[i]+D-1 < L[i+1] ならば、L[i]+D-1からL[i+1]-1までの壁は存在しない
    #L[i]+D-1 < L[i+1] ならば、L[i]+D-1からL[i+1]-1までの壁を破壊する
    #L[i]+D-1 < L[i+1] ならば、L[i]+D-1からL[i+1]-1までの壁を破壊する
    #L[i]+D-1 < L[i+1] ならば、L[i]+D-1からL[i+1]-1までの壁を破壊する
    #L[i]+D-1 < L[i+1] ならば、L[i]+D-

if __name__ == '__main__':
    main()