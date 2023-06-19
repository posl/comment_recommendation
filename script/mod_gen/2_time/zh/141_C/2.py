def main():
    n, k, q = map(int, input().split())
    a = []
    for i in range(q):
        a.append(int(input()))
    
    score = [k] * n
    for i in range(q):
        score[a[i]-1] += 1
    for i in range(n):
        if score[i] <= q:
            print('No')
        else:
            print('Yes')

if __name__ == '__main__':
    main()