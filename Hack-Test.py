
def meds (med_num):
    med_history = []
    med_count=1
    
    while (med_count < med_num+1):
        med_input = (raw_input("What is medication number " +str(med_count)+" "))
        med_history.append(med_input)
        med_count = med_count+1
    print ("These are your medications:",med_history)

    for i in range (0,med_num):
        intake_ans = str(raw_input("Did you take " +med_history[i]+" today? (y/n) ")) 
        
        if intake_ans == "y":
            print ("Great!")
            time = int(raw_input("When did you take it?- please enter in 24h clock: "))

        else:
            print("Don't forget to take them now!")
            
        i = i+1

def goals_achieved (goals_ans):
    goals =[]
    for i in range (0,goals_ans):
        goals.append(int(raw_input("What is goal number "+str(i+1)+"? - Enter '1' for Exercise, '2' for Diet, and '3' for Blood Glucose ")))
        i = i+1
    if 1 in goals:
        exercise_target = int(raw_input("How many hours of activity do you want to achieve this week? "))
        exercise_current = int(raw_input("How many hours were you active this week? "))
        
        if (exercise_current<exercise_target):
            print ("You have "+str(exercise_target-exercise_current)+" hours of activity to go!")
        else:
            print ("You have completed your goals, great work!!")
        
    if 2 in goals:
        vegetables_target=7
        meat_target=2
        dairy_target=2
        grains_target=6

        vegetables_current = int(raw_input("How many serving of vegatables did you take today? "))
        grains_current = int(raw_input("How many serving of grains did you take today? "))
        dairy_current = int(raw_input("How many serving of dairy did you take today? "))
        meat_current = int(raw_input("How many serving of meat did you take today? "))

        if (vegetables_current<vegetables_target):
            print ("You have "+str(vegetables_target-vegetables_current)+" servings to complete today's vegetables serving goal!")
        else:
            print ("You have completed your vegatable serving goals, great work!!")

        if (grains_current<grains_target):
            print ("You have "+str(grains_target-grains_current)+" servings to complete today's grains serving goal!")
        else:
            print ("You have completed your grains serving goals, great work!!")

        if (dairy_current<dairy_target):
            print ("You have "+str(dairy_target-dairy_current)+" servings to complete today's dairy serving goal!")
        else:
            print ("You have completed your dairy serving goals, great work!!")

        if (meat_current<meat_target):
            print ("You have "+str(meat_target-meat_current)+" servings to complete today's meat serving goal!")
        else:
            print ("You have completed your meat serving goals, great work!!")
        
    if 3 in goals:
        bg_target=8.5
        bg_current = float(raw_input("What is your current blood glucose level? "))

        if (bg_current>bg_target):
            print ("Glucose levels are too high by "+str(bg_current-bg_target)+" mmol/L")
        else:
            print ("You are at an optimal glucose level")
        
    
def details():
    name = (raw_input("What is your name?:"))
    print ("Hello "+name+"!")
    age = (raw_input("What is your age?:"))
    sex = (raw_input("What is your sex? (M/F/Specify Other:"))
    height = int(raw_input("What is your height in cm?:")) 
    weight = (raw_input("What is your weight in pounds (lbs)?:"))
##    exercise = int(raw_input("How many hours a day do you exercise?:"))
    dietary_res = str(raw_input("What are your dietary restrictions:?"))
    cholestrol = int(raw_input("What are your recent blood cholestrol levels from your last report:"))
    blood_glucose = float(raw_input("What are your recent blood glucose levels from your last report:"))
    blood_pressuresys = int(raw_input("What are your recent systolic blood pressure from your last report:"))
    blood_pressuredias = int(raw_input("What are your recent diastolic blood pressure from your last report:"))    
    med_num = int(raw_input("Number of medications?:"))
    meds (med_num)
    
    goals_ans = int(raw_input("Goals: (1) Exercise, (2)Diet, (3) Blood Glucose, How many of these goals do you want to focus on? Enter 1, 2, or 3 "))
    goals_achieved(goals_ans)
    
    
        
details()
