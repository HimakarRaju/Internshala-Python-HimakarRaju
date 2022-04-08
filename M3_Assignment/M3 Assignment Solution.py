#Importing score_calculator module
import score_calculator 


#Giving Inputs from dictionaries
p1={'name':'Virat Kohli', 'role':'bat', 'runs':112, '4':10, '6':0, 'balls':119, 'fielding':0} 
p2={'name':'du Plessis', 'role':'bat', 'runs':120, '4':11, '6':2, 'balls':112, 'fielding':0} 
p3={'name':'Bhuvneshwar Kumar', 'role':'bowl', 'wickets':1, 'overs':10, 'runs':71, 'fielding':1} 
p4={'name':'Yuzvendra Chahal', 'role':'bowl', 'wickets':2, 'overs':10, 'runs':45, 'fielding':0} 
p5={'name':'Kuldeep Yadav', 'role':'bowl', 'wickets':3, 'overs':10, 'runs':34, 'fielding':0}

# Making a list of dictionaries so that we can iterate through each dictionary
players = [p1,p2,p3,p4,p5]  

scores = {}

# Conditional Loop
for i in players:
    if i['role'] == 'bat':
        score = score_calculator.batting_score(i)
        scores[i['name']] = score
        print("'name':{},'batting_score':{}".format(i['name'],score))
    else:
        score = score_calculator.bowling_score(i)
        scores[i['name']] = score
        print("'name':{},'bowling_score':{}".format(i['name'],score))

max_scorer = max(scores,key=scores.get)

print("The maximum scorer is {} with score {}".format(max_scorer,max(scores.values())))
