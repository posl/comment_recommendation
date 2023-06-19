def main():
    N = int(input())
    A = []
    for i in range(N):
        a = int(input())
        A.append(a)
    for i in range(N):
        A.pop(i)
        print(max(A))
        A.insert(i, A.pop(i))
