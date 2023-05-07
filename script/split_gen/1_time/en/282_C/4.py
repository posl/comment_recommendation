def main():
    N = int(input())
    S = input()
    result = ""
    enclosed = False
    for i in range(N):
        if S[i] == '"':
            enclosed = not enclosed
            result += S[i]
        elif enclosed and S[i] == ',':
            result += S[i]
        elif not enclosed and S[i] == ',':
            result += '.'
        else:
            result += S[i]
    print(result)
