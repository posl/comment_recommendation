def main():
    # Get the input
    A, B, C = map(int, input().split())
    # Check if there is a number between A and B (inclusive) that is a multiple of C
    if A % C == 0:
        print(A)
    elif B % C == 0:
        print(B)
    else:
        # Find the first number between A and B (inclusive) that is a multiple of C
        for i in range(A+1, B+1):
            if i % C == 0:
                print(i)
                break
        else:
            print(-1)
