def main():
    N = int(input())
    data = []
    for i in range(N):
        S,P = input().split()
        data.append((S,int(P),i+1))
    data.sort(key=lambda x:(x[0],-x[1]))
    for i in range(N):
        print(data[i][2])
