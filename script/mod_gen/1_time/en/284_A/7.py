def main():
    N = int(input())
    list = []
    for i in range(N):
        list.append(input())
    for j in range(N):
        print(list[N-1-j])
main()
