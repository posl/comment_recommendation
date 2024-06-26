def main():
    N,W = map(int,input().split())
    water = [0] * (2*10**5+1)
    for i in range(N):
        S,T,P = map(int,input().split())
        water[S] += P
        water[T] -= P
    for i in range(1,2*10**5+1):
        water[i] += water[i-1]
    if max(water) > W:
        print("No")
    else:
        print("Yes")
