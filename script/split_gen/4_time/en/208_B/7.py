def main():
    p = int(input())
    coin_list = [1,2,6,24,120,720,5040,40320,362880,3628800]
    count = 0
    for i in reversed(coin_list):
        if p >= i:
            count += p // i
            p = p % i
    print(count)
