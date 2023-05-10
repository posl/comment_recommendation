def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    ans = []
    for i in range(q):
        x_i = x[i]
        ans.append(sum([abs(a_j-x_i) for a_j in a]))
    print(sum(ans))

if __name__ == '__main__':
    main()