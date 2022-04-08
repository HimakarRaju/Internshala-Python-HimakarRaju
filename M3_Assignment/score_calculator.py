# functions used for score calculation

# defining function for batting score
def batting_score(x):
    runs = x['runs']
    strike_rate = runs/x['balls']
    score = runs//2 + (5 if runs >= 50 else 0) + (10 if runs >= 100 else 0) + (2 if strike_rate >= 80/100 and strike_rate <= 1 else 0) + (4 if strike_rate > 1 else 0) + x['4'] + x['6']*2
    return score
    return {'name':x['name'],'batting_score':score}


# defining function for bowling score
def bowling_score(x):
    wickets = x['wickets']
    economy_rate = x['runs']/x['overs']
    fieldings=x['fielding']
    score = 10*wickets + (10*fieldings if fieldings>=1 else 0 ) +(5 if wickets>=3 else 0) + (10 if wickets>=5 else 0) + (4 if economy_rate>=3.5 and economy_rate<=4.5 else 0) + (7 if economy_rate>=2 and economy_rate<3.5 else 0) + (10 if economy_rate<2 else 0)
    return score
    return {'name':x['name'],'bowling_score':score}
