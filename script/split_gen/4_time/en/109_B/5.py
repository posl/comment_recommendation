def shiritori(n, words):
    if len(set(words)) == n and all(words[i][-1] == words[i+1][0] for i in range(n-1)):
        print("Yes")
    else:
        print("No")
