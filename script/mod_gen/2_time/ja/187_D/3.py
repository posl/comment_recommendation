def main():
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    
    diff = [a-b for a, b in zip(A, B)]
    diff.sort(reverse=True)
    
    count = 0
    for i in range(N):
        count += diff[i]
        if count > 0:
            print(i+1)
            exit()

if __name__ == '__main__':
    main()