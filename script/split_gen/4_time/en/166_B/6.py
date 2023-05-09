def main():
    input_list = input().split()
    N = int(input_list[0])
    K = int(input_list[1])
    d = []
    A = []
    for i in range(K):
        d.append(int(input()))
        A.append(input().split())
    print(N - K)
