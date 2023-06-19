def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    sum_A = sum(A)
    sum_B = sum(B)
    ans = sum_A/sum_B
    print(ans)
main()
