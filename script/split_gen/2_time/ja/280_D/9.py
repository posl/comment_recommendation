def main():
    K = int(input())
    #print(K)
    #print(type(K))
    
    #Kの約数を列挙
    divisor = []
    for i in range(1, int(K**0.5)+1):
        if K%i == 0:
            divisor.append(i)
            if i != K//i:
                divisor.append(K//i)
    #print(divisor)
    
    #約数の中から、Kと互いに素なものを列挙
    divisor2 = []
    for i in divisor:
        if gcd(i, K) == 1:
            divisor2.append(i)
    #print(divisor2)
    
    #約数の中から、Kと互いに素なものを列挙
    divisor3 = []
    for i in divisor:
        if gcd(i, K) == 1:
            divisor3.append(i)
    #print(divisor3)
    
    #Kと互いに素なものの中から、Kの倍数を作れるものを列挙
    divisor4 = []
    for i in divisor2:
        if K%i == 0:
            divisor4.append(i)
    #print(divisor4)
    
    #Kと互いに素なものの中から、Kの倍数を作れるものを列挙
    divisor5 = []
    for i in divisor3:
        if K%i == 0:
            divisor5.append(i)
    #print(divisor5)
    
    #最小のものを出力
    print(min(divisor4))
