def inciso1(names,scored_goals,prevented_goals,assists):
    players_stats={}
    for name,goal,prevented_goal,assist in zip(names,scored_goals,prevented_goals,assists):
        players_stats[name]={'Scored goals':goal,
                             'prevented goals':prevented_goal,
                             'assists':assist
                             }
    return players_stats
