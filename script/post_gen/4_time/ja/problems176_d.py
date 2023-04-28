Synthesizing 1/10 solutions

=======
Suggestion 1

def find_route(h, w, c_h, c_w, d_h, d_w, s):
    #print(h, w, c_h, c_w, d_h, d_w, s)
    #print(s)
    #print(s[c_h-1][c_w-1])
    #print(s[d_h-1][d_w-1])
    if s[c_h-1][c_w-1] == "#" or s[d_h-1][d_w-1] == "#":
        return -1
    if c_h == d_h and c_w == d_w:
        return 0
    #print("ok")
    #print(s)
    #print(s[c_h-1][c_w-1])
    #print(s[d_h-1][d_w-1])
    #print(c_h, c_w, d_h, d_w)
    #print(s[c_h-1][c_w-1])
    #print(s[d_h-1][d_w-1])
    #print("ok")
    #print("ok")
    #print(
