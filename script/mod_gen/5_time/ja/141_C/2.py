def main():
    n, k, q = map(int, input().split())
    a = [int(input()) for _ in range(q)]
    #print(n, k, q)
    #print(a)
    score = [0] * n
    for i in range(q):
        score[a[i]-1] += 1
    
    for i in range(n):
        if k - q + score[i] > 0:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()