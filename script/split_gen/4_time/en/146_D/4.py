def main():
    N = int(input())
    G = []
    for i in range(N-1):
        a, b = map(int, input().split())
        G.append([a,b])
    print(N-1)
    for i in range(N-1):
        print(i)
