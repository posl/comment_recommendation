def main():
    n,k = map(int,input().split())
    lr = []
    for i in range(k):
        lr.append(list(map(int,input().split())))
    print(n,k,lr)
