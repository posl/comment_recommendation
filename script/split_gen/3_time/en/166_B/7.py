def main():
    n,k = map(int,input().split())
    d = []
    for i in range(k):
        d.append(list(map(int,input().split())))
    d = [item for sublist in d for item in sublist]
    print(n-len(set(d[1:])))
