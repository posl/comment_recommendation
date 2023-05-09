def main():
    H = int(input())
    A = [H]
    while True:
        if A[-1] <= 1:
            break
        else:
            A.append(A[-1]//2)
    print(sum(A))
main()

if __name__ == '__main__':
    main()