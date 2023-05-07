def main():
    #input
    s,w = map(int,input().split())
    #output
    if s <= w:
        print("unsafe")
    else:
        print("safe")
