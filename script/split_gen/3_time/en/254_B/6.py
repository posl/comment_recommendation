def main():
    N = int(input())
    for i in range(N):
        print(" ".join([str(pascal(i, j)) for j in range(i + 1)]))
