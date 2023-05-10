def main():
    A,B,W = map(int,input().split())
    W = W * 1000
    ans = []
    for i in range(1,1001):
        if A * i <= W and W <= B * i:
            ans.append(i)
    if len(ans) == 0:
        print("UNSATISFIABLE")
    else:
        print(min(ans),max(ans))
