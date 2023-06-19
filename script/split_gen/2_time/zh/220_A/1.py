def main():
    # A B C = input().split()
    # A, B, C = int(A), int(B), int(C)
    # if A >= 1 and B >= A and B <= 1000 and C >= 1 and C <= 1000:
    #     for i in range(A, B+1):
    #         if i % C == 0:
    #             print(i)
    #             break
    # else:
    #     print(-1)
    A, B, C = map(int, input().split())
    for i in range(A, B+1):
        if i % C == 0:
            print(i)
            break
    else:
        print(-1)
