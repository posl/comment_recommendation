def main():
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    T = [list(map(int, input().split())) for _ in range(N)]
    #print(S)
    #print(T)
    # 一致判定
    def check():
        # Sの点を原点中心に270度回転させる
        S2 = []
        for s in S:
            S2.append([-s[1], s[0]])
        #print(S2)
        # S2の点をTの点に一致させる
        for t in T:
            #print(t)
            #print(S2)
            #print("----")
            #print([t[0] - s[0] for s in S2])
            #print([t[1] - s[1] for s in S2])
            if t[0] - S2[0][0] == t[1] - S2[0][1]:
                #print("OK")
                # S2の点を原点中心に270度回転させる
                S3 = []
                for s in S2:
                    S3.append([-s[1], s[0]])
                #print(S3)
                # S3の点をTの点に一致させる
                for t in T:
                    #print(t)
                    #print(S3)
                    #print("----")
                    #print([t[0] - s[0] for s in S3])
                    #print([t[1] - s[1] for s in S3])
                    if t[0] - S3[0][0] == t[1] - S3[0][1]:
                        #print("OK")
                        # S3の点を原点中心に270度回転させる
                        S4 = []
                        for s in S3:
                            S4.append([-s[1], s[0]])
                        #print(S4)
                        # S4の点をTの点に一致させる
                        for t in T:
                            #print(t)
                            #print(S4)
                            #print("----")
                            #print([t[0] - s
