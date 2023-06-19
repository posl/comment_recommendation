def check_shiritori():
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())
    for i in range(n-1):
        if words[i] == words[i+1]:
            return "No"
        if words[i][-1] != words[i+1][0]:
            return "No"
    return "Yes"
