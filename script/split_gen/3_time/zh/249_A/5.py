def main():
    A,B,C,D,E,F,X = map(int,input().split())
    taka = 0
    ao = 0
    for i in range(X):
        if i % (A + B + C) < A:
            taka += 1
        if i % (D + E + F) < D:
            ao += 1
    if taka > ao:
        print("高桥")
    elif taka < ao:
        print("青木")
    else:
        print("画")
