def contest_type(contest):
    if contest == "ABC":
        return "ARC"
    else:
        return "ABC"
contest = input()
print(contest_type(contest))
