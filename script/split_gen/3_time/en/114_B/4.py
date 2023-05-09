def main():
    S = input()
    result = 0
    for i in range(len(S)-2):
        temp = abs(753 - int(S[i:i+3]))
        if result == 0:
            result = temp
        elif temp < result:
            result = temp
    print(result)
