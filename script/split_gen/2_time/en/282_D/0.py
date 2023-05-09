def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        G[u-1].append(v-1)
        G[v-1].append(u-1)
    ans = 0
    for i in range(N):
        for j in G[i]:
            if j > i:
                ans += 1
                for k in G[j]:
                    if k > j:
                        if i not in G[k]:
                            ans += 1
    print(ans)
main()
I am not sure how to solve this problem. I have tried to use a 2D array to store the graph, but I am not sure how to do the second condition. Any help would be greatly appreciated.
Thanks
I am trying to write a program that will take a DNA sequence and find the longest common subsequence between the sequence and a list of sequences. I am having trouble with the longest common subsequence part. I have tried using dynamic programming and a recursive function but I am not getting the right result. I am not sure if I am doing it correctly. I am also not sure if I should be using dynamic programming or the recursive function.
Here is the code for the longest common subsequence using dynamic programming:
