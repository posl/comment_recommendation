def main():
    #input
    C1, C2, C3 = map(str, input().split())
    #compute
    #output
    if C1==C2 and C2==C3:
        print("Won")
    else:
        print("Lost")
