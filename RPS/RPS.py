def player(prev_play, opponent_history=[], play_order={}):
    if not prev_play:
        prev_play = 'R'

    opponent_history.append(prev_play)

    n=5

    if len(opponent_history) <=n:
        return "R"
    
    last_n_moves = "".join(opponent_history[-n:])

    if last_n_moves in play_order:
        play_order[last_n_moves] +=1
    else:
        play_order[last_n_moves] = 1

    potential_plays = [
        "".join(opponent_history[-(n-1):]) + "R",
        "".join(opponent_history[-(n-1):]) + "P",
        "".join(opponent_history[-(n-1):]) + "S",
    ]

    sub_order = {
        k: play_order.get(k,0)
        for k in potential_plays
    }

    prediction = max(sub_order, key=sub_order.get)[-1]

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}

    return ideal_response[prediction]