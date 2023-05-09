def main():
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    AB = []
    for a in A:
        for b in B:
            AB.append(a+b)
    AB.sort(reverse=True)
    ABC = []
    for ab in AB[:K]:
        for c in C:
            ABC.append(ab+c)
    ABC.sort(reverse=True)
    for i in range(K):
        print(ABC[i])
main()
I got AC. I think this solution is not so efficient because I used 3 nested loops. But I couldn’t find any other way to solve this problem. If you have any idea, please let me know.
Thank you for reading my blog.
