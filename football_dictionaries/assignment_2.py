def players_by_position(squads_list):
    grouped_by_position = {}

    
    for player in squads_list:
        position = player['position']
        if position not in grouped_by_position:
            grouped_by_position[position] = []
        
        grouped_by_position[position].append(player)
    
    return grouped_by_position
