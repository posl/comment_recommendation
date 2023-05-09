def solve():
    S1 = input()
    S2 = input()
    S3 = input()
    N1 = len(S1)
    N2 = len(S2)
    N3 = len(S3)
    if N1 < N3 and N2 < N3:
        print("UNSOLVABLE")
        return
    def check(S1,S2,S3):
        for i in range(len(S1)):
            if S1[i] == S2[i] and S1[i] != S3[i]:
                return False
            if S1[i] == S3[i] and S1[i] != S2[i]:
                return False
            if S2[i] == S3[i] and S1[i] != S2[i]:
                return False
        return True
    def solve(S1,S2,S3):
        ans = []
        for i in range(10):
            for j in range(10):
                for k in range(10):
                    if S1[0] == "0" and i == 0:
                        continue
                    if S2[0] == "0" and j == 0:
                        continue
                    if S3[0] == "0" and k == 0:
                        continue
                    S1_ = str(i)*N1
                    S2_ = str(j)*N2
                    S3_ = str(k)*N3
                    if check(S1_,S2_,S3_):
                        ans.append((S1_,S2_,S3_))
        return ans
    ans = solve(S1,S2,S3)
    if len(ans) == 0:
        print("UNSOLVABLE")
    else:
        print(ans[0][0])
        print(ans[0][1])
        print(ans[0][2])
