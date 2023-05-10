def main():
    # input
    A, B, C, D, E = map(int, input().split())
    # compute
    # output
    if (A==B and C==D) or (A==B and C==E) or (A==B and D==E) or (A==C and B==D) or (A==C and B==E) or (A==C and D==E) or (A==D and B==C) or (A==D and B==E) or (A==D and C==E) or (A==E and B==C) or (A==E and B==D) or (A==E and C==D) or (B==C and A==D) or (B==C and A==E) or (B==C and D==E) or (B==D and A==C) or (B==D and A==E) or (B==D and C==E) or (B==E and A==C) or (B==E and A==D) or (B==E and C==D) or (C==D and A==B) or (C==D and A==E) or (C==D and B==E) or (C==E and A==B) or (C==E and A==D) or (C==E and B==D) or (D==E and A==B) or (D==E and A==C) or (D==E and B==C):
        print('Yes')
    else:
        print('No')
