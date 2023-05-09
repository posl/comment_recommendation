def main():
    N,K = map(int,input().split())
    h = list(map(int,input().split()))
    counter = 0
    for i in range(N):
        if h[i]>=K:
            counter+=1
    print(counter)
