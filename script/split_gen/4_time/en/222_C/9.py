def get_player_rank(player_id, matches):
    player_win_count = 0
    for match in matches:
        if match[0] == player_id or match[1] == player_id:
            player_win_count += 1
    return player_win_count
