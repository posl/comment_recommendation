def main():
    #N is an integer.
    #1 ≦ N ≦ 30
    N = int(input())
    #If he will wear white N days later, print White; if he will wear black, print Black.
    print("White" if N%2==0 else "Black")
