def main():
    # Get input
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    # Get output
    ans = []
    for i in range(q):
        ans.append(len(list(filter(lambda y: y >= x[i], a))))
    # Print output
    for i in range(q):
        print(ans[i])
