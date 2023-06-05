def main():
    num = input().split()
    P = int(num[0])
    Q = int(num[1])
    R = int(num[2])
    print(min(P+Q, Q+R, R+P))
