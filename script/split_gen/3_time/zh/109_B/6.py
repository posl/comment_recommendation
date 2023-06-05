def main():
    N = int(input())
    words = []
    for i in range(N):
        words.append(input())
    if len(words) == len(set(words)) and len(set([i[0] for i in words])) == len(words):
        print("Yes")
    else:
        print("No")
