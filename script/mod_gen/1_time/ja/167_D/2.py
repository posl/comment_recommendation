def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = [i - 1 for i in a]
    #print(a)
    visited = [0] * n
    num = 0
    while k > 0:
        if visited[num] == 1:
            break
        visited[num] = 1
        num = a[num]
        k -= 1
    #print(num)
    #print(visited)
    if k == 0:
        print(num + 1)
    else:
        loop = 0
        for i in range(n):
            if visited[i] == 1:
                loop += 1
        k %= loop
        #print(loop)
        #print(k)
        for i in range(k):
            num = a[num]
        print(num + 1)

if __name__ == '__main__':
    main()