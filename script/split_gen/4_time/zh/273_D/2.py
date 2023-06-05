def main():
    h,w,r_s,c_s = map(int,input().split())
    n = int(input())
    r_c = [map(int,input().split()) for _ in range(n)]
    q = int(input())
    d_l = [input().split() for _ in range(q)]
    r_c = [[r,c] for r,c in r_c]
    d_l = [[d,int(l)] for d,l in d_l]
    for d,l in d_l:
        if d == "L":
            c_s -= l
        elif d == "R":
            c_s += l
        elif d == "U":
            r_s -= l
        elif d == "D":
            r_s += l
        print(r_s,c_s)
