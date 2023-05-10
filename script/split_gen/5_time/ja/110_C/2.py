def main():
    S = list(input())
    T = list(input())
    S.sort()
    T.sort(reverse=True)
    if S < T:
        print("Yes")
    else:
        print("No")
