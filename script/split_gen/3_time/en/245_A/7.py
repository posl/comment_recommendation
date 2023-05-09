def main():
    # Read input
    A,B,C,D = [int(x) for x in input().split()]
    # Process
    if A*60+B < C*60+D+1:
        print("Takahashi")
    else:
        print("Aoki")
