def get_time(i, j, N, T, K, path, visited, sum, count):
    if i == 0 and j == 0 and sum == K and count == N:
        return 1
    else:
        res = 0
        for k in range(N):
            if visited[k] == 0:
                visited[k] = 1
                path.append(k)
                res += get_time(j, k, N, T, K, path, visited, sum + T[j][k], count + 1)
                path.pop()
                visited[k] = 0
        return res

if __name__ == '__main__':
    get_time()