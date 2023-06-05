def search(city, time, k, n, visited):
    if time > k:
        return 0
    if len(visited) == n:
        if time == k:
            return 1
        else:
            return 0
    ans = 0
    for i in range(n):
        if i in visited:
            continue
        visited.append(i)
        ans += search(i, time+city[i], k, n, visited)
        visited.pop()
    return ans
n, k = map(int, input().split())
city = []
for i in range(n):
    city.append(list(map(int, input().split())))
ans = search(0, 0, k, n, [0])
print(ans)

if __name__ == '__main__':
    search()