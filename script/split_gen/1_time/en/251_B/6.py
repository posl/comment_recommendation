def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    #print(A)
    a = A[0]
    b = A[1]
    c = A[2]
    d = A[3]
    e = A[4]
    f = A[5]
    g = A[6]
    count = 0
    for i in range(W//a + 1):
        for j in range((W - a*i)//b + 1):
            for k in range((W - a*i - b*j)//c + 1):
                for l in range((W - a*i - b*j - c*k)//d + 1):
                    for m in range((W - a*i - b*j - c*k - d*l)//e + 1):
                        for n in range((W - a*i - b*j - c*k - d*l - e*m)//f + 1):
                            for o in range((W - a*i - b*j - c*k - d*l - e*m - f*n)//g + 1):
                                if a*i + b*j + c*k + d*l + e*m + f*n + g*o <= W:
                                    count += 1
                                else:
                                    break
    print(count)
