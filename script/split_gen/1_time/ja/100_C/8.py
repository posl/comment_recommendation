def main():
    #入力
    N = int(input())
    a = list(map(int,input().split()))
    
    cnt = 0
    while True:
        for i in range(N):
            if a[i] % 2 == 0:
                a[i] = a[i] / 2
            else:
                print(cnt)
                return
        cnt += 1
