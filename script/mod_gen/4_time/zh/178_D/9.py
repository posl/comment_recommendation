def count_seq_sum(s):
    #s = 7
    #s = 1729
    #s = 2
    count = 0
    for i in range(3,s+1):
        if i == s:
            count += 1
            break
        if i > s:
            break
        for j in range(3,s+1):
            if i+j == s:
                count += 1
                break
            if i+j > s:
                break
            for k in range(3,s+1):
                if i+j+k == s:
                    count += 1
                    break
                if i+j+k > s:
                    break
                for l in range(3,s+1):
                    if i+j+k+l == s:
                        count += 1
                        break
                    if i+j+k+l > s:
                        break
                    for m in range(3,s+1):
                        if i+j+k+l+m == s:
                            count += 1
                            break
                        if i+j+k+l+m > s:
                            break
                        for n in range(3,s+1):
                            if i+j+k+l+m+n == s:
                                count += 1
                                break
                            if i+j+k+l+m+n > s:
                                break
                            for o in range(3,s+1):
                                if i+j+k+l+m+n+o == s:
                                    count += 1
                                    break
                                if i+j+k+l+m+n+o > s:
                                    break
                                for p in range(3,s+1):
                                    if i+j+k+l+m+n+o+p == s:
                                        count += 1
                                        break
                                    if i+j+k+l+m+n+o+p > s:
                                        break
                                    for q in range(3,s+1):
                                        if i+j+k+l+m+n+o+p+q == s:
                                            count += 1
                                            break
                                        if i+j+k+l+m+n+o+p+q > s:
                                            break
                                        for r in range(3,s+1):
                                            if i+j+k+l+m+n+o+p+q+r == s:
                                                count += 1
                                                break
                                            if i+j+k+l+m+n+o+p+q+r > s:
                                                break
                                            for t in range(3,s+1):
                                                if i+j

if __name__ == '__main__':
    count_seq_sum()