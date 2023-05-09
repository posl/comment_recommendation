def main():
    #Get input from standard input
    A, B, C = map(int, input().split())
    #Determine whether A^2 + B^2 < C^2 holds
    if (A**2 + B**2) < (C**2):
        print("Yes")
    else:
        print("No")
main()
