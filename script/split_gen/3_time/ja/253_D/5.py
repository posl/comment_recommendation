def main():
    N, A, B = map(int, input().split())
    # 3の倍数の総和
    s3 = A*(N//A)*(N//A+1)//2
    # 5の倍数の総和
    s5 = B*(N//B)*(N//B+1)//2
    # 15の倍数の総和
    s15 = A*B*(N//(A*B))*(N//(A*B)+1)//2
    print(s3+s5-s15)
