def main():
    A,B,W = map(int, input().split())
    W *= 1000
    ans = []
    for i in range(1,1001):
        if A*i <= W <= B*i:
            ans.append(i)
    if ans == []:
        print("UNSATISFIABLE")
    else:
        print(ans[0], ans[-1])
