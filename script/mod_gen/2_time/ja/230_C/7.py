def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    # 1 つめの操作で塗るマスの数
    num1 = min(N - A, B - 1) + 1
    # 2 つめの操作で塗るマスの数
    num2 = min(N - A, N - B) + 1
    # 1 つめの操作で塗るマスのうち、P≦ i≦ Q をみたすマスの数
    num3 = max(0, min(Q, N - A) - max(P, A) + 1)
    # 2 つめの操作で塗るマスのうち、P≦ i≦ Q をみたすマスの数
    num4 = max(0, min(Q, N - A) - max(P, A - N + B + 1) + 1)
    # 1 つめの操作で塗るマスのうち、R≦ j≦ S をみたすマスの数
    num5 = max(0, min(S, B) - max(R, B - N + A + 1) + 1)
    # 2 つめの操作で塗るマスのうち、R≦ j≦ S をみたすマスの数
    num6 = max(0, min(S, N - B) - max(R, B) + 1)
    # 1 つめの操作で塗るマスのうち、P≦ i≦ Q かつ R≦ j≦ S をみたすマスの数
    num7 = max(0, min(Q, N - A) - max(P, A) + 1) * max(0, min(S, B) - max(R, B - N + A + 1) + 1)
    # 2 つめの操作で塗るマスのうち、P≦ i≦ Q かつ R≦ j≦ S をみたすマスの数
    num8

if __name__ == '__main__':
    main()