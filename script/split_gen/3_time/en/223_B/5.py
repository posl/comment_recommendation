def main():
    S = input()
    T = S+S
    S_min = T
    S_max = ""
    for i in range(len(S)):
        S_max = max(S_max, T[i:i+len(S)])
        S_min = min(S_min, T[i:i+len(S)])
    print(S_min)
    print(S_max)
