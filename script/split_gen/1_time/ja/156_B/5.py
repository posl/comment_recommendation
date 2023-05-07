def main():
    n,k = map(int,input().split()) #nをk進数で表したときの桁数を求める
    cnt = 0
    while n != 0:
        n //= k
        cnt += 1
    print(cnt)
