def main():
    #Get the input
    A, B = map(int, input().split())
    #Print the largest number among A + B, A - B, and A × B.
    print(max(A + B, A - B, A * B))

if __name__ == '__main__':
    main()