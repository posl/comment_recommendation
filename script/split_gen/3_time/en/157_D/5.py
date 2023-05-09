def main():
    # Input
    N, M, K = map(int, input().split())
    A = [0] * M
    B = [0] * M
    C = [0] * K
    D = [0] * K
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    for i in range(K):
        C[i], D[i] = map(int, input().split())
    
    # Solve
    # Initialize
    # Each user has no friend candidate
    ans = [0] * N
    # Each user has no friend
    friends = [set() for i in range(N)]
    # Each user has no blockship
    blockships = [set() for i in range(N)]
    
    # Input friends
    for i in range(M):
        a = A[i] - 1
        b = B[i] - 1
        # Add friendship
        friends[a].add(b)
        friends[b].add(a)
    
    # Input blockships
    for i in range(K):
        c = C[i] - 1
        d = D[i] - 1
        # Add blockship
        blockships[c].add(d)
        blockships[d].add(c)
    
    # Calculate friend candidates
    # For each user
    for i in range(N):
        # Calculate the number of users who are not friends of the user
        # and who are not blocked by the user
        ans[i] = N - len(friends[i]) - 1
        # Calculate the number of users who are blocked by the user
        for j in blockships[i]:
            # If the user is blocked by the user
            if i in friends[j]:
                # The user is not a friend candidate
                ans[i] -= 1
    
    # Output
    print(*ans)
    
    return
