def main():
    # P = int(input())
    # Q = int(input())
    # R = int(input())
    P, Q, R = map(int, input().split())
    print(min(P+Q, Q+R, R+P))
