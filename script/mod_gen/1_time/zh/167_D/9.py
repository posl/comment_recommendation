def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    visited = [False]*n
    visited[0] = True
    count = 1
    next = a[0]-1
    while not visited[next]:
        visited[next] = True
        next = a[next]-1
        count += 1
    k = k%count
    next = 0
    while k>0:
        next = a[next]-1
        k -= 1
    print(next+1)

if __name__ == '__main__':
    main()