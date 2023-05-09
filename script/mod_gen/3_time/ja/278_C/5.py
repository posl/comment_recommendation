def follow(user, follow)
  user = user - 1
  follow = follow - 1
  $follows[user][follow] = true
  $follows[follow][user] = true
end

if __name__ == '__main__':
    follow()