def main():
    n,k=map(int,input().split())
    sushi=[]
    for _ in range(n):
        sushi.append(list(map(int,input().split())))
    sushi.sort(key=lambda x:x[1],reverse=True)
    sushi.sort(key=lambda x:x[0])
    print(sushi)
