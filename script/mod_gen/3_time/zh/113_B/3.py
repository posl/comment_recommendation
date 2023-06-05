def main():
    N = int(input())
    T,A = map(int,input().split())
    H = list(map(int,input().split()))
    h = [abs(T - H[i] * 0.006 - A) for i in range(N)]
    print(h.index(min(h)) + 1)
main()
