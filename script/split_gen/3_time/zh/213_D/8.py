def main():
    N = int(input())
    A = [0] * (N-1)
    B = [0] * (N-1)
    for i in range(N-1):
        A[i], B[i] = map(int, input().split())
    #print(N)
    #print(A)
    #print(B)
    #print("end")
    visited = [0] * N
    visited[0] = 1
    route = [1]
    city = 1
    while True:
        for i in range(N-1):
            if A[i] == city and visited[B[i]-1] == 0:
                visited[B[i]-1] = 1
                city = B[i]
                route.append(city)
                break
            elif B[i] == city and visited[A[i]-1] == 0:
                visited[A[i]-1] = 1
                city = A[i]
                route.append(city)
                break
        else:
            if city == 1:
                break
            else:
                for i in range(N-1):
                    if A[i] == city:
                        city = B[i]
                        route.append(city)
                        break
                    elif B[i] == city:
                        city = A[i]
                        route.append(city)
                        break
    print(*route)
