def main():
    N = int(input())
    S = input()
    if N % 2 == 0:
        print(S.replace(",", "."))
    else:
        print("error")
