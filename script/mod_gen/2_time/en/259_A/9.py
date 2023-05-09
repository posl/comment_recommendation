def main():
    #Read the input
    N, M, X, T, D = map(int, input().split())
    #Calculate the height
    if M < X:
        height = T + (X - M) * D
    else:
        height = T
    #Print the answer
    print(height)

if __name__ == '__main__':
    main()