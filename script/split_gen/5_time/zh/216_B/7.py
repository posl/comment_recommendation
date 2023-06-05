def main():
    N = int(input())
    name = []
    for i in range(N):
        name.append(input())
    if len(name) != len(set(name)):
        print("Yes")
    else:
        print("No")
