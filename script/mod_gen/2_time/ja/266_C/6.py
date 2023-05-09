def main():
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    D = list(map(int, input().split()))
    # 3点のなす角度を求める
    def angle(A, B, C):
        # 内積
        ab = (B[0]-A[0]) * (C[0]-B[0]) + (B[1]-A[1]) * (C[1]-B[1])
        # 外積
        ac = (B[0]-A[0]) * (C[1]-B[1]) - (B[1]-A[1]) * (C[0]-B[0])
        return np.arctan2(ac, ab) * 180 / np.pi
    # 3点のなす角度の和を求める
    angle_sum = angle(A, B, C) + angle(B, C, D) + angle(C, D, A) + angle(D, A, B)
    if angle_sum == 360:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()