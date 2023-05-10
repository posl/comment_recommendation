def main():
    N,A,B = map(int,input().split())
    # 1~Nまでの和
    sumN = N*(N+1)//2
    # Aの倍数の和
    sumA = A*(N//A)*((N//A)+1)//2
    # Bの倍数の和
    sumB = B*(N//B)*((N//B)+1)//2
    # AとBの公倍数の和
    sumAB = (A*B)*((N//(A*B))+1)//2
    print(sumN - sumA - sumB + sumAB)
