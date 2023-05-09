def main():
    #input
    S, W = map(int, input().split())
    
    #output
    if W >= S:
        print("unsafe")
    else:
        print("safe")
