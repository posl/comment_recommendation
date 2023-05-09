def main():
    N = int(input())
    names = []
    for i in range(N):
        names.append(input())
    if len(set(names)) == N:
        print("No")
    else:
        print("Yes")
