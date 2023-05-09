def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    # print(x)
    if n >= m:
        print(0)
        return
    diff = []
    for i in range(m-1):
        diff.append(x[i+1]-x[i])
    diff.sort()
    # print(diff)
    print(sum(diff[:m-n]))
