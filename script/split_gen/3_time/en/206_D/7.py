def main():
    N = int(input())
    A = list(map(int, input().split()))
    
    #Aの要素の個数を数える
    count = [0] * (200001)
    for a in A:
        count[a] += 1
    
    #Aの要素の個数が奇数のものの個数を数える
    odd = 0
    for c in count:
        if c % 2 == 1:
            odd += 1
    
    #Aの要素の個数が奇数のものの個数が0のときは0
    if odd == 0:
        print(0)
        return
    
    #Aの要素の個数が奇数のものの個数が1のときはN-1
    if odd == 1:
        print(N-1)
        return
    
    #Aの要素の個数が奇数のものの個数が2以上のときはN-odd
    print(N-odd)
main()
