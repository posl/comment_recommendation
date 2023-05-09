def main():
    N, K = map(int, input().split())
    S = []
    for _ in range(N):
        S.append(input())
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            Sij = S[i] + S[j]
            Sij = set(Sij)
            if len(Sij) < K:
                continue
            for k in range(j+1, N):
                Sijk = S[i] + S[j] + S[k]
                Sijk = set(Sijk)
                if len(Sijk) < K:
                    continue
                for l in range(k+1, N):
                    Sijkl = S[i] + S[j] + S[k] + S[l]
                    Sijkl = set(Sijkl)
                    if len(Sijkl) < K:
                        continue
                    for m in range(l+1, N):
                        Sijklm = S[i] + S[j] + S[k] + S[l] + S[m]
                        Sijklm = set(Sijklm)
                        if len(Sijklm) < K:
                            continue
                        for n in range(m+1, N):
                            Sijklmn = S[i] + S[j] + S[k] + S[l] + S[m] + S[n]
                            Sijklmn = set(Sijklmn)
                            if len(Sijklmn) < K:
                                continue
                            for o in range(n+1, N):
                                Sijklmno = S[i] + S[j] + S[k] + S[l] + S[m] + S[n] + S[o]
                                Sijklmno = set(Sijklmno)
                                if len(Sijklmno) < K:
                                    continue
                                for p in range(o+1, N):
                                    Sijklmnop = S[i] + S[j] + S[k] + S[l] + S[m] + S[n] + S[o] + S[p]
                                    Sijklmnop = set(Sijklmnop)
                                    if len(Sijklmnop) < K:
                                        continue
                                    for q in range(p+1, N):
                                        Sijklmnopq = S[i] + S[j] + S[k] + S[l] + S[m] + S[n] + S[o] + S[p] + S[q]
                                        Sijklmnopq = set

if __name__ == '__main__':
    main()