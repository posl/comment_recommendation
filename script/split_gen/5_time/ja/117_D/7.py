def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    #print(n, k)
    #print(a)
    #print()
    
    #kの上位ビットを求める
    k_bit = 0
    while k > 0:
        k_bit += 1
        k //= 2
        #print(k)
    #print(k_bit)
    #print()
    
    #aの上位ビットを求める
    a_bit = [0]*n
    for i in range(n):
        tmp_a = a[i]
        while tmp_a > 0:
            a_bit[i] += 1
            tmp_a //= 2
            #print(tmp_a)
        #print(a_bit[i])
    #print()
    
    #kの上位ビットとaの上位ビットの最大値を求める
    max_bit = 0
    for i in range(n):
        if max_bit < a_bit[i]:
            max_bit = a_bit[i]
    if max_bit < k_bit:
        max_bit = k_bit
    #print(max_bit)
    #print()
    
    #kの上位ビットとaの上位ビットの最大値を求める
    max_bit = 0
    for i in range(n):
        if max_bit < a_bit[i]:
            max_bit = a_bit[i]
    if max_bit < k_bit:
        max_bit = k_bit
    #print(max_bit)
    #print()
    
    #kの上位ビットとaの上位ビットの最大値を求める
    max_bit = 0
    for i in range(n):
        if max_bit < a_bit[i]:
            max_bit = a_bit[i]
    if max_bit < k_bit:
        max_bit = k_bit
    #print(max_bit)
    #print()
    
    #kの上位ビットとaの上位ビットの最大値を求める
    max_bit = 0
    for i in range(n):
        if max_bit < a_bit[i]:
            max_bit = a_bit[i]
    if max_bit < k_bit:
        max_bit = k_bit
    #print(max_bit)
