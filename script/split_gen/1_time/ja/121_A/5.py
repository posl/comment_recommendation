def main():
    h, w = map(int, input().split())
    h_p, w_p = map(int, input().split())
    print((h*w)-(h_p*w)-(h*w_p)+(h_p*w_p))
