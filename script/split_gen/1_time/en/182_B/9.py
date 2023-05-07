def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 2以上の整数の中で、GCD-nessが最大になるものを出力する
    # GCD-ness: Aの要素のうち、kで割り切れるものの数
    # 2以上の整数の中で、GCD-nessが最大になるものは、Aの要素の最大公約数である
    # まず、Aの最大公約数を求める
    # ただし、Aの要素がすべて同じ場合は、出力はAの要素のどれか1つでよい
    maxGCD = A[0]
    for a in A:
        maxGCD = gcd(maxGCD, a)
    # Aの要素がすべて同じ場合は、出力はAの要素のどれか1つでよい
    if maxGCD == A[0]:
        print(A[0])
        return
    # Aの最大公約数を出力する
    print(maxGCD)
