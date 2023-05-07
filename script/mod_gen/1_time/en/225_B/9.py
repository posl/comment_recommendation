def main():
    N = int(input())
    edges = [list(map(int, input().split())) for _ in range(N-1)]
    #print(edges)
    #print([i[0] for i in edges])
    #print([i[1] for i in edges])
    #print(set([i[0] for i in edges]))
    #print(set([i[1] for i in edges]))
    #print(set([i[0] for i in edges]) & set([i[1] for i in edges]))
    if len(set([i[0] for i in edges]) & set([i[1] for i in edges])) == 1:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()