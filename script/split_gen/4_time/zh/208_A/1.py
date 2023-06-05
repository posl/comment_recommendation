def main():
    A, B = map(int, input().split())
    for i in range(1, A+1):
        for j in range(1, A+1):
            if i + j == B:
                print("Yes")
                return
    print("No")
    return
