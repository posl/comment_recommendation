def main():
    # read the input
    A, B, C, D, E = map(int, input().split())
    # print the answer
    print(len(set([A, B, C, D, E])))

if __name__ == '__main__':
    main()