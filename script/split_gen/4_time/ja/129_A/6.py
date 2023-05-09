def main():
    # P, Q, R = map(int, input().split())
    # print(min(P+Q, Q+R, R+P))
    print(min([sum(x) for x in zip(map(int, input().split()), map(int, input().split()), map(int, input().split()))]))
