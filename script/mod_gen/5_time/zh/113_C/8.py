def main():
    N, M = map(int, input().split())
    P_Y = [list(map(int, input().split())) for _ in range(M)]
    P_Y.sort(key=lambda x:(x[0], x[1]))
    P_Y_dict = {}
    for i, (P, Y) in enumerate(P_Y):
        P_Y_dict[P] = P_Y_dict.get(P, []) + [(Y, i)]
    for P, Y in P_Y:
        print('{:06d}{:06d}'.format(P, P_Y_dict[P].index((Y, P_Y_dict[P].index((Y, i)))) + 1))

if __name__ == '__main__':
    main()