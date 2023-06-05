def main():
    N,M = map(int,input().split())
    B = [list(map(int,input().split())) for _ in range(N)]
    if N > 10:
        print("No")
        return
    if M > 7:
        print("No")
        return
    for i in range(1,100):
        for j in range(1,8):
            if B[0][0] == (i-1)*7+j:
                if B[0][1] == (i-1)*7+j+1:
                    if B[0][2] == (i-1)*7+j+2:
                        if B[1][0] == (i)*7+j:
                            if B[1][1] == (i)*7+j+1:
                                if B[1][2] == (i)*7+j+2:
                                    print("Yes")
                                    return
    print("No")
