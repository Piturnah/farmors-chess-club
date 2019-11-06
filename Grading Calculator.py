import csv

def Calc_Grades():
    with open("grades.csv") as grades:
        grades_reader = list(csv.reader(grades, delimiter=","))
        
        for player in grades_reader:
            if player[0] == "id":
                pass # skip entry if it's the first entry
            else:
                player_performance = [] # list of performance grades
                
                if len(player) >= 5:
                    print(player)
                    for i in range (3, len(player) - 1):
                        if i % 2 != 0:
                            opponent_grade = grades_reader[int(player[i])][2]
                            print(opponent_grade)
        grades.close()

Calc_Grades()
