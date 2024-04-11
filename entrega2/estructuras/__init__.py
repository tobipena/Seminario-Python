def players_names_and_stats(names:list[str],scored_goals:list[int],prevented_goals:list[int],assists:list[int]) -> dict:
    '''  devuelve un dict donde se asocian todas las estadisticas a su respectivo jugador  '''
    players_stats={}
    for name,goal,prevented_goal,assist in zip(names,scored_goals,prevented_goals,assists):
        players_stats[name]={'scored goals':goal,
                             'prevented goals':prevented_goal,
                             'assists':assist
                             }
    return players_stats

def players_names_and_goals(players_stats:dict) -> dict:
    '''  devuelve un dict donde la clave es el nombre del jugador y el valor son sus goles convertidos  '''
    players_goals={key: value['scored goals'] for key, value in players_stats.items()}
    return players_goals

def players_names_and_influence(players_stats:dict) -> dict:
    '''  devuelve un dict donde la clave es el nombre del jugador y el valor es su influencia segun sus estadisticas  '''
    players_influence={}
    for player,stats in players_stats.items():
        players_influence[player]=(stats['scored goals']*1.5 + stats['prevented goals']*1.25 + stats['assists'])/3
    return players_influence
