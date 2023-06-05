def weather():
    N = int(input())
    S = input()
    if S[N-1] == "o":
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    weather()