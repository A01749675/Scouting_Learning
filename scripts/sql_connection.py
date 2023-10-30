import mysql.connector as MySQL

host_name = 'localhost'
user_name = 'root'
password = 'root'
db ='scout'
connection = MySQL.connect(host=host_name, user=user_name, passwd=password, db=db)
cur = connection.cursor(buffered=True)

parameters = ['timestamp','team','match_number','primary_score','secondary_score','endgame']

def register_match(values):
    global connection,cur
    entry = []
    columns = ""
    for key,value in values.items():
        entry.append(value)
        columns+=str(key)+","
    columns = columns[:len(columns)-1]
    query = ("INSERT into matches ("+columns+") VALUES (%s,%s,%s,%s,%s)")
    try:
        cur.execute(query,entry)
        connection.commit()
    except Exception as e:
        print(e)

def get_team_avg_stats(team):
    global connection,cur
    result = {}
    parameters = ["primary_score","secondary_score","endgame"]
    query=("SELECT AVG(primary_score), AVG(secondary_score), AVG(endgame)  from matches WHERE team ="+str(team))
    try:
        cur.execute(query)
        connection.commit()
        leg_no = cur.fetchall()
        for i in range(len(leg_no)):
            result[parameters[i]]=leg_no[i]
    except Exception as e:
        print(e)
    return result

def get_team_matches(team):
    global connection,cur
    query = ("SELECT * from matches WHERE team = "+str(team))
    try:
        cur.execute(query)
        connection.commit()
        result = cur.fetchall()
        print(result)
    except Exception as e:
        print(e)


register_match({'team':3478,'match_number':3,'primary_score':27,'secondary_score':14,'endgame':20})

print(get_team_avg_stats(3478))

get_team_matches(3478)
