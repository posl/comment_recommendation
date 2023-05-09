def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    diff = []
    for i in range(N):
        diff.append(abs(x[i] - X))
    #print(diff)
    #print(gcd_list(diff))
    print(gcd_list(diff))
