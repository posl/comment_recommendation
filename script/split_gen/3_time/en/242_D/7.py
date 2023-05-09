def main():
    S = input()
    Q = int(input())
    for _ in range(Q):
        t, k = map(int, input().split())
        #print(t, k)
        print(S[(k-1)%len(S)])
