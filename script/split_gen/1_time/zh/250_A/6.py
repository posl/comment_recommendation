def main():
    H,W = map(int,input().split())
    R,C = map(int,input().split())
    print(H*W-((H-R)*W+(W-C)*R))
