def main():
    N = int(input())
    a = [0] * (N-1)
    b = [0] * (N-1)
    for i in range(N-1):
        a[i],b[i] = map(int,input().split())
    #print(a)
    #print(b)
    if a.count(a[0]) == N-1:
        print("Yes")
    elif b.count(b[0]) == N-1:
        print("Yes")
    else:
        print("No")
