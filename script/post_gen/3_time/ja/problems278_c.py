Synthesizing 10/10 solutions

=======
Suggestion 1

def follow(followers, user1, user2)
  if followers[user1] == nil
    followers[user1] = [user2]
  else
    followers[user1].push(user2)
  end
end

=======
Suggestion 2

def parent(x):
    if par[x] == x:
        return x
    else:
        par[x] = parent(par[x])
        return par[x]

=======
Suggestion 3

def find_root(x)
  return x if @parent[x] == x
  @parent[x] = find_root(@parent[x])
  return @parent[x]
end

=======
Suggestion 4

def follow(user1, user2):
    if user1 == user2:
        return False
    if user1 in users[user2]:
        return True
    return False

=======
Suggestion 5

def init_par(n):
    par = {}
    for i in range(1, n + 1):
        par[i] = i
    return par

=======
Suggestion 6

def follow(user, follow)
  user = user - 1
  follow = follow - 1
  $follows[user][follow] = true
  $follows[follow][user] = true
end

=======
Suggestion 7

def follow?(a, b)
  if $follows[a][b]
    puts 'Yes'
  else
    puts 'No'
  end
end

=======
Suggestion 8

def follow(i, j)
  @follows[i] << j
  @follows[j] << i
end

=======
Suggestion 9

def follow(followers, a, b)
  followers[a] << b
end

=======
Suggestion 10

def follow?(a, b)
  $follow[a].include?(b)
end
