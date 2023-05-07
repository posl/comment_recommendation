def main():
    A, B = map(int, input().split())
    #AとBの最大公約数を求める
    def gcd(a, b):
        if a%b == 0:
            return b
        else:
            return gcd(b, a%b)
    #AとBの最大公約数を求める
    G = gcd(A, B)
    #Gの約数を求める
    def divisor(n):
        i = 1
        table = []
        while i*i <= n:
            if n%i == 0:
                table.append(i)
                if i != n//i:
                    table.append(n//i)
            i += 1
        return table
    #Gの約数の個数を求める
    print(len(divisor(G)))
