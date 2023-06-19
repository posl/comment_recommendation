def solve(w):
    if w <= 3:
        return [1, 2, 3][:w]
    else:
        ans = [1, 2, 3]
        if w % 2 == 0:
            ans.append(2)
        else:
            ans.append(3)
        if w % 2 == 0:
            for i in range(w // 4 - 1):
                ans.extend([4, 5])
            if w % 4 == 2:
                ans.append(4)
        else:
            for i in range(w // 4 - 1):
                ans.extend([4, 5])
            ans.append(6)
        return ans

if __name__ == '__main__':
    solve()