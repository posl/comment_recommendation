def main():
    #Read Input
    N, K = map(int, input().split())
    p = sorted(list(map(int, input().split())))
    #Main Logic
    ans = sum(p[:K])
    #Print Output
    print(ans)
