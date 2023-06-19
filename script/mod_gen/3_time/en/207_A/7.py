def main():
    # Read the input
    A,B,C = map(int,input().split())
    # Find the maximum of the sum of two cards
    print(max(A+B,A+C,B+C))
main()
