player1 = 'Gullit'
player2 = 'Van Basten'

goal_1 = 32
goal_2 = 54

scorers = player1 +' ' +str(goal_1) +',' +' ' + player2 +' ' + str(goal_2)
print (scorers)

report = (
player1
+' '
+'scored in the'
+' '
+str(goal_1)
+'nd minute'
+'\n'
+player2
+' '
+'scored in the'
+' '
+str(goal_2)
+'th minute'
)
print (report)

name = 'Ronald Koeman'
first_name = name[0:6]
print (first_name)

last_name_len = len(name[7:13])
print(last_name_len)

name_short = name[0] +'.' +' ' + name[7:13]
print(name_short)

crowd = 'Go'
chant = (crowd+ ' ' +first_name+'!'+' ')*6
print (chant.rstrip())


good_chant = chant[35] != ' '
print (good_chant)
