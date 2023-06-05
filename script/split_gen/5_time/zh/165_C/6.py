def get_score(N,M,Q,ABCD):
    max_score = 0
    for i in range(1,M+1):
        for j in range(1,M+1):
            for k in range(1,M+1):
                for l in range(1,M+1):
                    score = 0
                    for m in range(1,N+1):
                        for n in range(1,N+1):
                            for o in range(1,N+1):
                                for p in range(1,N+1):
                                    for q in range(1,N+1):
                                        for r in range(1,N+1):
                                            for s in range(1,N+1):
                                                for t in range(1,N+1):
                                                    for u in range(1,N+1):
                                                        for v in range(1,N+1):
                                                            for w in range(1,N+1):
                                                                for x in range(1,N+1):
                                                                    for y in range(1,N+1):
                                                                        for z in range(1,N+1):
                                                                            if m < n < o < p < q < r < s < t < u < v < w < x < y < z:
                                                                                if ABCD[0][0] <= m <= ABCD[0][1]:
                                                                                    if ABCD[1][0] <= n <= ABCD[1][1]:
                                                                                        if ABCD[2][0] <= o <= ABCD[2][1]:
                                                                                            if ABCD[3][0] <= p <= ABCD[3][1]:
                                                                                                if ABCD[4][0] <= q <= ABCD[4][1]:
                                                                                                    if ABCD[5][0] <= r <= ABCD[5][1]:
                                                                                                        if ABCD[6][0] <= s <= ABCD[6][1]:
                                                                                                            if ABCD[7][0] <= t <= ABCD[7][1]:
                                                                                                                if ABCD[8][0] <= u <= ABCD[8][1]:
                                                                                                                    if ABCD[9][0] <= v <= ABCD[9][1]:
                                                                                                                        if ABCD[10][0] <= w <= ABCD[10][1]:
                                                                                                                            if ABCD[11][0] <= x <= ABCD[11][1]:
                                                                                                                                if ABCD[12][0] <= y <= ABCD
