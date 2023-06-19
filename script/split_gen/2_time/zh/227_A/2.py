def main():
    n,k,a = map(int,input().split())
    res = (k+a-1) % n
    if res == 0:
        print(n)
    else:
        print(res)
