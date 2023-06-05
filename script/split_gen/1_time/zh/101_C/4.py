def main():
    n,k = input().split()
    n = int(n)
    k = int(k)
    a = input().split()
    a = list(map(int,a))
    cnt = 0
    for i in range(n-k+1):
        cnt += 1
    print(cnt)
