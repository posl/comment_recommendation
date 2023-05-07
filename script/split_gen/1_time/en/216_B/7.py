def main():
    names = []
    for i in range(int(input())):
        names.append(input())
    if len(set(names)) == len(names):
        print("No")
    else:
        print("Yes")
