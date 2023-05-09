def main():
    N = int(input())
    A = [0] * (N-1)
    B = [0] * (N-1)
    for i in range(N-1):
        A[i],B[i] = map(int,input().split())
    #print(A)
    #print(B)
    #print(N)
    #print(A)
    #print(B)
    #都市の数だけリストを作成
    city = [[] for i in range(N)]
    #print(city)
    #都市の数だけリストを作成
    for i in range(N-1):
        city[A[i]-1].append(B[i])
        city[B[i]-1].append(A[i])
    #print(city)
    #都市の数だけリストを作成
    visited = [0] * N
    #print(visited)
    #都市の数だけリストを作成
    ans = [0] * N
    #print(ans)
    #都市の数だけリストを作成
    ans[0] = 1
    #print(ans)
    #都市の数だけリストを作成
    visited[0] = 1
    #print(visited)
    #都市の数だけリストを作成
    current = 0
    #print(current)
    #都市の数だけリストを作成
    for i in range(N-1):
        #print(i)
        #print(city)
        #print(visited)
        #print(ans)
        #print(current)
        #都市の数だけリストを作成
        for j in city[current]:
            #print(j)
            #print(visited)
            #print(ans)
            #print(current)
            #都市の数だけリストを作成
            if visited[j-1] == 0:
                #都市の数だけリストを作成
                ans[i+1] = j
                #都市の数だけリストを作成
                visited[j-1] = 1
                #都市の数だけリストを作成
                current = j-1
                #都市の数だけリストを作成
                break
