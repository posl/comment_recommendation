def main():
    #input
    a, b, c, d, e = map(int, input().split())
    #output
    print(len(set([a, b, c, d, e])))
