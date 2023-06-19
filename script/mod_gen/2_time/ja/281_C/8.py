def main():
    #input
    N, T = map(int, input().split())
    As = list(map(int, input().split()))
    #compute
    #Aの合計値
    Asum = sum(As)
    #Aの合計値で割った余り
    T %= Asum
    #Aの合計値で割った商
    Quotient = T // Asum
    #TをAの合計値で割った余りで割った商
    Quotient2 = Quotient // N
    #TをAの合計値で割った余りで割った余り
    Remainder = Quotient % N
    #TをAの合計値で割った余りで割った余りをAの合計値で割った商にかけたもの
    Quotient3 = Remainder * Quotient2
    #TをAの合計値で割った余りで割った余りをAの合計値で割った商にかけたものをAの合計値で割った余りに足したもの
    Remainder2 = Quotient3 + (T % Asum)
    #TをAの合計値で割った余りで割った余りをAの合計値で割った商にかけたものをAの合計値で割った余りに足したものをAの合計値で割った余りで割った商
    Quotient4 = Remainder2 // Asum
    #TをAの合計値で割った余りで割った余りをAの合計値で割った商にかけたものをAの合計値で割った余りに足したものをAの合計値で割った余りで割った余り
    Remainder3 = Remainder2 % Asum
