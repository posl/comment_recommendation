def main():
    n, q = map(int, input().split())
    a = [int(i) for i in input().split()]
    k = [int(input()) for _ in range(q)]
    for i in k:
        count = 0
        for j in range(1, 10**18):
            if j not in a:
                count += 1
            if count == i:
                print(j)
                break
