def main():
    # Get input here
    n,a,b = [int(x) for x in input().strip().split()]
    # Calculate result here
    result = 0
    # Print output here
    for i in range(n):
        for j in range(a):
            for k in range(n):
                for l in range(b):
                    if (i+k)%2==0:
                        print(".",end="")
                    else:
                        print("#",end="")
                print("")
    return 0
