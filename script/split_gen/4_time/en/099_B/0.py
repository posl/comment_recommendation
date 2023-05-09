def main():
    # input
    a, b = map(int, input().split())
    # compute
    # output
    print(int((b-a)*(b-a+1)/2-b))
