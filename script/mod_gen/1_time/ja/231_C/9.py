def main():
    #入力
    #N,Q = map(int, input().split())
    #A = list(map(int, input().split()))
    #X = [int(input()) for _ in range(Q)]
    N,Q = 5,5
    A = [804289384, 846930887, 681692778, 714636916, 957747794]
    X = [424238336, 719885387, 649760493, 596516650, 189641422]
    
    #Aの要素をソート
    A.sort()
    
    #Xの要素を昇順にソート
    X.sort()
    
    #Aの要素を二分探索
    for x in X:
        print(bisect.bisect_left(A, x))

if __name__ == '__main__':
    main()