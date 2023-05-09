def shiritori():
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())
    if len(words) != len(set(words)):
        print("No")
    else:
        for i in range(n-1):
            if words[i][-1] != words[i+1][0]:
                print("No")
                break
        else:
            print("Yes")
shiritori()

if __name__ == '__main__':
    shiritori()