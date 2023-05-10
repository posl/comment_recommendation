def main():
    N = int(input())
    S = input()
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabets = alphabets * 2
    result = ""
    for i in range(len(S)):
        index = alphabets.find(S[i])
        result += alphabets[index + N]
    print(result)
