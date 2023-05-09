def follow(followers, user1, user2)
  if followers[user1] == nil
    followers[user1] = [user2]
  else
    followers[user1].push(user2)
  end
end
