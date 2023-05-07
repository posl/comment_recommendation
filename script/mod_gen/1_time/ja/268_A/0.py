def main():
    A, B, C, D, E = map(int, input().split())
    print(len(set([A, B, C, D, E])))

if __name__ == '__main__':
    main()