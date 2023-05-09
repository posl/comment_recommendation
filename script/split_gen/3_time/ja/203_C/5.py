def main():
    n,k = map(int,input().split())
    ab = []
    for i in range(n):
        a,b = map(int,input().split())
        ab.append([a,b])
    ab.sort()
    for i in range(n):
        a,b = ab[i]
        if k < a:
            break
        else:
            k += b
    print(k)
