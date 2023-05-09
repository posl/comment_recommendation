def main():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    for i in range(N):
        for j in range(B[i]+1):
            if A[i]*j == X:
                print("Yes")
                return
            elif A[i]*j > X:
                break
            else:
                X = X - A[i]*j
                for k in range(N):
                    for l in range(B[k]+1):
                        if A[k]*l == X:
                            print("Yes")
                            return
                        elif A[k]*l > X:
                            break
                        else:
                            X = X - A[k]*l
                            for m in range(N):
                                for n in range(B[m]+1):
                                    if A[m]*n == X:
                                        print("Yes")
                                        return
                                    elif A[m]*n > X:
                                        break
                                    else:
                                        X = X - A[m]*n
                                        for o in range(N):
                                            for p in range(B[o]+1):
                                                if A[o]*p == X:
                                                    print("Yes")
                                                    return
                                                elif A[o]*p > X:
                                                    break
                                                else:
                                                    X = X - A[o]*p
                                                    for q in range(N):
                                                        for r in range(B[q]+1):
                                                            if A[q]*r == X:
                                                                print("Yes")
                                                                return
                                                            elif A[q]*r > X:
                                                                break
                                                            else:
                                                                X = X - A[q]*r
                                                                for s in range(N):
                                                                    for t in range(B[s]+1):
                                                                        if A[s]*t == X:
                                                                            print("Yes")
                                                                            return
                                                                        elif A[s]*t > X:
                                                                            break
                                                                        else:
                                                                            X = X - A[s]*t
                                                                            for u in range(N):
                                                                                for v in range(B[u]+1):
                                                                                    if A[u]*v == X:
                                                                                        print("Yes")
                                                                                        return
                                                                                    elif A[u]*v > X:
                                                                                        break
                                                                                    else:
                                                                                        X = X - A[u]*v
                                                                                        for w in range(N):
                                                                                            for x in range(B[w]+1):
                                                                                                if A[w]*x == X:
                                                                                                    print("Yes")
                                                                                                    return
