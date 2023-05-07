def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    # 1文字目が一致するものを取得
    for s in S:
        for t in T:
            if s[0] == t[0]:
                # 2文字目が一致するものを取得
                for s2 in S:
                    for t2 in T:
                        if s[1] == t[1] and s2[1] == t2[1]:
                            # 3文字目が一致するものを取得
                            for s3 in S:
                                for t3 in T:
                                    if s[2] == t[2] and s2[2] == t2[2] and s3[2] == t3[2]:
                                        # 4文字目が一致するものを取得
                                        for s4 in S:
                                            for t4 in T:
                                                if s[3] == t[3] and s2[3] == t2[3] and s3[3] == t3[3] and s4[3] == t4[3]:
                                                    # 5文字目が一致するものを取得
                                                    for s5 in S:
                                                        for t5 in T:
                                                            if s[4] == t[4] and s2[4] == t2[4] and s3[4] == t3[4] and s4[4] == t4[4] and s5[4] == t5[4]:
                                                                # 6文字目が一致するものを取得
                                                                for s6 in S:
                                                                    for t6 in T:
                                                                        if s[5] == t[5] and s2[5] == t2[5] and s3[5] == t3[5] and s4[5] == t4[5] and s5[5] == t5[5] and s6[5] == t6[5]:
                                                                            # 7文字目が一致するものを取得
                                                                            for s7 in S:
                                                                                for t7 in T:
