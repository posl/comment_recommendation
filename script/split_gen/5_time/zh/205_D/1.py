def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    k = []
    for i in range(q):
        k.append(int(input()))
    for i in range(q):
        count = 0
        for j in range(1, 10**18):
            if j not in a:
                count += 1
                if count == k[i]:
                    print(j)
                    break
