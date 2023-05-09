def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = [i-1 for i in a]
    #print(n, k, a)
    
    # 遷移先を記録
    memo = [0] * n
    memo[0] = a[0]
    for i in range(1, n):
        memo[i] = memo[i-1] + a[i]
        memo[i] %= n
    
    #print(memo)
    
    # 最初の繰り返し
    tmp = [0] * n
    for i in range(n):
        tmp[memo[i]] += 1
    #print(tmp)
    
    # 繰り返し
    for i in range(k):
        tmp2 = [0] * n
        for j in range(n):
            tmp2[memo[j]] += tmp[j]
        tmp = tmp2
        #print(tmp)
    
    print(tmp[0]+1)
