def main():
    H, W = map(int, input().split())
    S = [list(input()) for i in range(H)]
    #print(S)
    # 1. count the number of '.'s
    count = 0
    for h in range(H):
        for w in range(W):
            if S[h][w] == '.':
                count += 1
    # 2. find the maximum distance from any '.' to any '.'
    max_dist = 0
    for h in range(H):
        for w in range(W):
            if S[h][w] == '.':
                dist = 0
                for hh in range(H):
                    for ww in range(W):
                        if S[hh][ww] == '.':
                            dist = max(dist, abs(h-hh) + abs(w-ww))
                max_dist = max(max_dist, dist)
    #print(count, max_dist)
    print(max_dist)

if __name__ == '__main__':
    main()