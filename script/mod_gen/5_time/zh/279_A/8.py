def count_d(S):
    count = 0
    for i in range(len(S)):
        if S[i] == "v":
            for j in range(i+1, len(S)):
                if S[j] == "w":
                    count += 1
    return count

if __name__ == '__main__':
    count_d()