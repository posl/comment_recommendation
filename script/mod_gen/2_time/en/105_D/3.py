def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a % M for a in A]
    A = [0] + A
    for i in range(N):
        A[i+1] = (A[i+1] + A[i]) % M
    from collections import defaultdict
    D = defaultdict(int)
    for a in A:
        D[a] += 1
    ans = 0
    for d in D.values():
        ans += d * (d-1) // 2
    print(ans)
main()
I think the problem is that I am using defaultdict(int) , but I don't know how to use defaultdict(list) .
I tried defaultdict(list) and append() , but it doesn't work.
I have a list of tuples, each tuple has a name and a value. I want to sort the list by the value, and if the value is the same, sort by the name.
I have tried to use the following code:

if __name__ == '__main__':
    main()