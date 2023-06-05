def main():
    n, q = map(int, input().split())
    seq = []
    for i in range(n):
        seq.append(list(map(int, input().split()))[1:])
    for i in range(q):
        s, t = map(int, input().split())
        print(seq[s-1][t-1])
main()
