def main():
    N = int(input())
    A = list(map(int,input().split()))
    mod = [ [] for i in range(200) ]
    for i in range(N):
        mod[A[i]%200].append(i+1)
    for i in range(200):
        if len(mod[i]) >= 2:
            print("Yes")
            print(len(mod[i]),*mod[i])
            print(len(mod[i])-1,*mod[i][:-1])
            return
    print("No")
