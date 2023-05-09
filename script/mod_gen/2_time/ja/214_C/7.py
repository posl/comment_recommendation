def main():
    N = int(input())
    S = list(map(int,input().split()))
    T = list(map(int,input().split()))
    #Sの最大値
    maxS = max(S)
    #Tの最小値
    minT = min(T)
    #Tの最小値がSの最大値を超えたら、最小値を最大値にする
    if minT > maxS:
        minT = maxS
    #Tの最小値を超えるSの値を取り除く
    S = list(filter(lambda x: x > minT,S))
    #Tの最小値を超えるTの値を取り除く
    T = list(filter(lambda x: x > minT,T))
    #Tの最小値を超えるSの値の最小値
    minS = min(S)
    #Tの最小値を超えるSの値の最小値を超えるTの値を取り除く
    T = list(filter(lambda x: x > minS,T))
    #Tの最小値を超えるSの値の最小値を超えるTの値の最小値
    minT = min(T)
    #Tの最小値を超えるSの値の最小値を超えるTの値の最小値を超えるSの値を取り除く
    S = list(filter(lambda x: x > minT,S))
    #Tの最小値を超えるSの値の最小値を超えるTの値の最小値を超えるSの値の最小値
    minS = min(S)
    #Tの最小値を超えるSの値の最小値を超えるTの値の最小値を超えるSの値の最小値を超えるTの値を取り除く
    T = list(filter(lambda x: x > minS,T))
    #Tの最小値

if __name__ == '__main__':
    main()