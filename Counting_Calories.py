# -*- coding: cp1252 -*-
import csv
import time
#START OF COUNTING CALORIES PART 2
def CountingCaloriesPart2(age):
    #SCORE COUNTER DICTIONARY
    mydict={'A':1,'B':2,'C':3}
    #Questions for all Age Groups
    #AGES 0-4
    questions={'How much time does your child spend doing physical exercise daily?':['A)My child doesn’t exercise','B)1-3 hours','C)Greater than 3 hours']
                     ,'What physical activity does your child get involved in?':['A)Playing with toys','B)skipping','C)Ball games'],
                      'How does your child normally spend their weekend?':['A)Playing on electronic devices (tablets/smartphones)','B)Riding their bike','C)Playing in the park'],
                      'What method of transportation does your child use to travel to Preschool/Nursery?':['A)Car','B)Walking','C)Riding their bike'],
                      'What are your child’s interest?':['A)Watching television','B)Playing and socialising with other children','C)Outdoor Activities']}
    #AGES 5-18
    questions1={'How long do you spend using your mobile phone or electronic device?':['A)Greater than 5 hours','B)Between 2-5 hours','C)Less than 2 hours'],
                       'How do you normally travel to school/college everyday?':['A)car/bus/train','B)Walk to school/college','C)Riding their bike'],
                       'What is your favourite pastime?':['A)Playing Videogames/Arts and Crafts','B)Meeting and socialising with friends','C)Going Outdoors(Hiking/Camping)'],
                       'How much time do you spend doing physical exercise daily?':['A)I don’t exercise','B))Less than 1 hour ','C)greater than 1 hour'],
                       'What extra-curricular activity do you participate in School/College?':['A)I don’t participate in any extra-curricular activity','B)Performing in school plays','C)Representing my school in a team sport']
                       }
    #AGES 19-64 if a)
    questions2={
                       'How would you describe the nature of your occupation?':['A)IT Administrative, Office Work','B) Semi-labour intensive manual work(retail, mechanic, operating machinery)','C)Very-labour intensive(argriculture,construction)'],
                       'How often are you outdoors?':['A)Rarley','B)Most of the Time','C)All The Time'],
                       'How much time do you spend exercising daily?':['A)I don’t exercise','B)Between 1 and 2 hours','C)More than 2 hours'],
                       'How long do you spend using your mobile phone or electronic device?':['A)Greater than 5 hours','B)Between 2-5 hours','C)Less than 2 hours'],
                       'What is your favourite pastime?':['A)Meeting and socialising with friends','B)Going for walks','C)Exercising at the Gym']}

    #AGES 19-64 if b)
    questions3={
                       'How do you occupy your time?':['A)Staying Indoors','B)Higher Education(University)','C)Engaging in Sports/Volunteering'],
                       'How often are you outdoors?':['A)Rarley','B)Most of the Time','C)All The Time'],
                       'How much time do you spend exercising daily?':['A)I don’t exercise','B)Between 1 and 2 hours','C)More than 2 hours'],
                       'How long do you spend using your mobile phone or electronic device?':['A)Greater than 5 hours','B)Between 2-5 hours','C)Less than 2 hours'],
                       'What is your favourite pastime?':['A)Meeting and socialising with friends','B)Going for walks','C)Exercising at the Gym']}
    #AGES 65-76
    questions4={
                       'How much time do you spend exercising daily?':['A)I don’t exercise at all','B)Less than 30 minutes','C)More than 30 minutes'],
                       'How intense would you describe the physical activities you do?':['A)Light','B)Moderate','C)High Impact'],
                       'What physical activities do you do ?':['A)Pilates/Yoga','B)Walking','C)Ballroom Dancing'],
                       'How often do you leave your home?':['A)Rarely','B)Sometimes','C)Most of the Time'],
                       'What is your favourite pastime?':['A)Watching films/TV','B)Meeting and socialising with friends','C)Playing a Sport']}
    score=0
    if 0<age<75:
        if 0<=age<=4 :
            for question,options in questions.iteritems():
                print "\nQuestion:\n\n",question
                for opt in options:
                    print opt
                a=raw_input('\nEnter Your Choice: ') 
                if a in mydict: score=score+mydict[a]   
        elif 4<age<=18 :
            for question,options in questions1.iteritems():
                print "\nQuestion:\n\n",question
                for opt in options:
                    print opt
                a=raw_input('\nEnter Your Choice: ')
                if a in mydict: score=score+mydict[a]
        elif 18<age<=64 :
            employ=raw_input('\nAre you currently employed?\nA)Yes\nB)No\n\nEnter Your Choice: ')
            if employ=='A':
                for question,options in questions2.iteritems():
                    print "\nQuestion:\n\n",question
                    for opt in options:
                        print opt
                    a=raw_input('\nEnter Your Choice: ')
                    if a in mydict: score=score+mydict[a]
            elif employ=='B':
                for question,options in questions3.iteritems():
                    print "\nQuestion:\n\n",question
                    for opt in options:
                        print opt
                    a=raw_input('\nEnter Your Choice: ')
                    if a in mydict: score=score+mydict[a]
        elif 65<age<=75:
            for question,options in questions4.iteritems():
                    print "\nQuestion:\n\n",question
                    for opt in options:
                        print opt
                    a=raw_input('\nEnter Your Choice: ')
                    if a in mydict: score=score+mydict[a]    
    #Determining the Lifestyle after points have been collected            
    if 0<age<76:
        print 'You Scored:',score
        if score<=8:
             result='Sedentary'
        elif score>=9 and score<=12:
             result='Moderately Active'
        else:
            result = 'Active'
    return result,score
#MAIN MENU FOR PART 2 COUNTING CALORIES
def MainMenuPart2(name,filename, age, gender):
    count=5
    ch=True
    while ch!=0 and count>0:
        print'''=========================MAIN MENU=======================
            

                                                                    Welcome Back''', name,'''!

                                                                     1. START (PART 2)
                                                                     2. INSTRUCTIONS
                                                                     3. ABOUT
                                                                     0. BACK (When Finished Part 2)

                                                                     
================================================================'''
        ch=input('Enter a Choice: ')
        if ch==1:
            Lifestyle,score=CountingCaloriesPart2(age)
            print "Your lifestyle is:", Lifestyle
            cals=recommcals(filename, age, gender, Lifestyle)
        elif ch==2:
            print('''================================INSTRUCTIONS========================

            How Part 2 Works:


                 1. Fill in Our questionairre
                 2. Get Your Lifestyle 
                 3. Determine if you're eating the reccomended calories for your age and lifestyle
    
                ================================================================ ''')

        elif ch==3:
            print('''===============================INFORMATION==========================

            Counting Calories:

                 Counting Calories is designed to compare the Calories
                 you are consuming daily,with the lifestyle you live.This
                 will assess whether you're eating the reccomended Calories
                 or not.

        ===================================================================''')
        elif str(ch) not in "0123":
            count-=1
            print '\nINVALID ENTRY.\nAttempts Remaining:',count
            if count==0:
                time.sleep(1)
                print 'Goodbye...'
    return cals,score
#END OF CountingCaloriesPart2
#START OF SNACKS FUNCTION
def SnackMenu(Options):
    scals=0
    Snackitems=[]
    time.sleep(1)
    o=open('Snacks.txt','r')
    for row in o:
        print (row.strip('\n'))
    b=raw_input('Enter Your Choice: ')
    while b!='S' and count<3:
        caloriecount=Options[b]
        scals=caloriecount
        if b in Options.keys():
            if b=='A':
                Snackitems.append('Walnuts')
                break
            elif b=='B':
                Snackitems.append('Pita Bread & Hummus')
                break
            elif b=='C':
                Snackitems.append('Apple with Peanut Butter')
                break
            elif b=='D':
                Snackitems.append('2 Salted Packets of Crisps')
                break
            elif b=='E':
                Snackitems.append('Triple Chocolate Muffin ')
                break
            elif b=='F':
                Snackitems.append('Cheddar with 4 Triscuits + Red/White Wine')
                break
            elif b=='G':
                Snackitems.append('Chocolate Coconut Chia Seed Pudding')
                break
            elif b=='H':
                Snackitems.append('2 Chocolate Muffins')
                break
            elif b=='I':
                Snackitems.append('1 Chocolate Brownie')
                break
            elif b=='J':
                Snackitems.append('Cheese Nachos and Beans')
                break
            elif b=='K':
                Snackitems.append('Chili Cheese Fries')
                break
            elif b=='L':
                Snackitems.append('Chocolate Coconut Chia Seed Pudding + Pita Bread Hummus')
                break
    return  Snackitems,scals
#START OF DESSERTS FUNCTION
def DessertMenu(Options):
        descals=0
        Dessertitems=[]
        time.sleep(1)
        o=open('Desserts.txt','r')
        for row in o:
            print (row.strip('\n'))
        b=raw_input('\n\nEnter Your Choice: ')
        while b!='S' and count<3:
            caloriecount=Options[b]
            descals=caloriecount
            if b in Options.keys():
                if b=='A':
                    Dessertitems.append('Vanilla Ice Cream')
                    break
                elif b=='B':
                    Dessertitems.append('Chocolate Mousse')
                    break
                elif b=='C':
                    Dessertitems.append('Coconut Banana Cream Pies')
                    break
                elif b=='D':
                    Dessertitems.append('Chocolate Bread Pudding')
                    break
                elif b=='E':
                    Dessertitems.append('Vanilla Cheesecake')
                    break
                elif b=='F':
                    Dessertitems.append('2 Galub Jamen & 2 Fruit Salads')
                    break
                elif b=='G':
                    Dessertitems.append('Blueberry Banana Crepes')
                    break
                elif b=='H':
                    Dessertitems.append('Cookie Dough with Milk Chocolate')
                    break
                elif b=='I':
                    Dessertitems.append('Carrot Cake')
                    break
                elif b=='J':
                    Dessertitems.append('Lemon Cake')
                    break
                elif b=='K':
                    Dessertitems.append('Brownies & Ice Cream')
                    break
                elif b=='L':
                    Dessertitems.append('Hot Fudge Stuffed Cookie')
                    break
        return Dessertitems,descals
#START OF DINNER FUNCTION
def DinnerMenu(Options):
        dcals=0
        Dinneritems=[]
        time.sleep(1)
        o=open('Dinner.txt','r')
        for row in o:
            print (row.strip('\n'))
        b=raw_input('\n\nEnter Your Choice: ')
        while b!='S':
            caloriecount=Options[b]
            dcals=caloriecount
            if b in Options.keys():
                if b=='A':
                    Dinneritems.append('Vegetable Stir-Fry')
                    break
                elif b=='B':
                    Dinneritems.append('Chicken Stir-Fry')
                    break
                elif b=='C':
                    Dinneritems.append('Meat Lasagne')
                    break
                elif b=='D':
                    Dinneritems.append('Itsu-Chicken + Noodle Soup')
                    break
                elif b=='E':
                    Dinneritems.append('Oven Baked Fish & Chips ')
                    break
                elif b=='F':
                    Dinneritems.append('Chicken Casserole')
                    break 
                elif b=='G':
                    Dinneritems.append('Double Cheeseburger')
                    break
                elif b=='H':
                    Dinneritems.append('Roasted Apple & Chedder Salad with Roasted Chicken + Gravy with Shredded root Vegetables')
                    break
                elif b=='I':
                    Dinneritems.append('Cod with Tomato Cream Sauce')
                    break
                elif b=='J':
                    Dinneritems.append('Chicken Katsu-Curry')
                    break
                elif b=='K':
                    Dinneritems.append('Spicy Salmon + Lentils')
                    break
                elif b=='L':
                    Dinneritems.append('Tuna avacado + quinoa salad')
                    break
        return Dinneritems,dcals
#START OF LUNCH MENU FUNCTION
def LunchMenu(Options):
        lcals=0
        Lunchitems=[]
        time.sleep(1)
        o=open('Lunch.txt','r')
        for row in o:
            print (row.strip('\n'))
        b=raw_input('Enter Your Choice: ')
        while b!='S':
            caloriecount=Options[b]
            lcals=caloriecount
            if b in Options.keys():
                if b=='A':
                    Lunchitems.append('Courgette Pea & Pesto Soup')
                    break
                elif b=='B':
                    Lunchitems.append('Mexican Quinoa')
                    break
                elif b=='C':
                    Lunchitems.append('Meat Lasagne')
                    break
                elif b=='D':
                    Lunchitems.append('Cereal with Milk, 2 Digestive Biscuits')
                    break
                elif b=='E':
                    Lunchitems.append('Jacket Potato')
                    break
                elif b=='F':
                    Lunchitems.append('Bacon Lettuce & Tomato Sandwich')
                    break
                elif b=='G':
                    Lunchitems.append('Ceaser Turkey Wrap')
                    break
                elif b=='H':
                    Lunchitems.append('Chicken Fajita Wrap')
                    break
                elif b=='I':
                    Lunchitems.append('Aspragus and Tuna Salad')
                    break
                elif b=='J':
                    Lunchitems.append('Ground Chicken & Boiled Mashed Sweet Potato')
                    break
                elif b=='K':
                    Lunchitems.append('Beef Stew & Dumplings')
                    break
                elif b=='L':
                    Lunchitems.append('Creamy Pasta with Asparagus & Peas')
                    break
        return Lunchitems,lcals
#START OF BREAKFAST MENU FUNCTION
def BreakfastMenu(Options):
    bcals=0
    breakfastitems=[]
    o=open('Breakfast.txt','r')
    for row in o:
        print (row.strip('\n'))
    b=raw_input('\nEnter Your Choice: ')
    while b !='S':
        caloriecount=Options[b]
        bcals=caloriecount
        if b in Options.keys():
            if b=='A':
                breakfastitems.append('Plain Toast, Milk, 1 Chocolate Biscuit')
                break
            elif b=='B':
                breakfastitems.append('Cereal with Milk, Toast with Butter')
                break
            elif b=='C':
                breakfastitems.append('Plain Yoghurt, Apple Juice, 2 Apricots')
                break
            elif b=='D':
                breakfastitems.append('Cereal with Milk, 2 Digestive Biscuits')
                break
            elif b=='E':
                breakfastitems.append('2 Toasts with Peanut Butter, Coffee')
                break
            elif b=='F':
                breakfastitems.append('Apple, Banana, Toast with Honey, Coffee')
                break
            elif b=='G':
                breakfastitems.append('Plum, Orange, Peach, Blueberry Muffin, Pineapple Juice')
                break
            elif b=='H':
                breakfastitems.append('Scrambled Eggs, Baked Beans, Strawberries, Tea with 1 Sugar')
                break
            elif b=='I':
                breakfastitems.append('Waffles, 1.5 Apples, Orange Juice')
                break
            elif b=='J':
                breakfastitems.append('Porridge, Banana, Plum, Peach, Blueberry Muffin, Milk')
                break
            elif b=='K':
                breakfastitems.append('Sausage, Baked Beans, Scrambled eggs, 4 Apricots')
                break
            elif b=='L':
                breakfastitems.append('Oatmeal, Pancakes, Tropical Fruit Salad, Green Tea with Lemon and Honey')
                break
    return breakfastitems, bcals
#PERSONAL INFORMATION to be used in PART 2 of the program
#NAME PROCEDURE
def Name():
    count=5
    print'\nWelcome User.\nEnter your details before starting Part1:'
    name=raw_input('\nName: ')
    while name=='' and count>1:
        count-=1
        print 'INVALID ENTRY.\nAttempts Remaining:',count
        name=raw_input('\nName: ')
    if name=='':
        print 'Name defaulted to "User1"'
        name="User1" 
    return name
#AGE PROCEDURE
def Age():
    print'\nEnter an age value between 0-75.'
    age=input('Age:')
    while (age<0 or age>75):
        print 'INVALID ENTRY.\nEnter a Value Between 0-75.'
        age=input('\nAge:')
    return age
#GENDER PROCEDURE
def Gender():
    print'\nEnter Gender (M/F)'
    gender=raw_input('Gender: ')
    while gender!='M' and gender!='F':
        print '\nINVALID ENTRY.\nEnter "M" for Male or "F" for Female'
        gender=raw_input('\nGender: ')
    print '\n STARTING PART 1...'
    time.sleep(1)
    return gender
#FINDING THE RECOMMENDED CALORIE COUNT BASED ON AGE,GENDER AND LIFESTYLE
def recommcals(filename, age, gender, Lifestyle):
    row={}
    recommcal=0
    f=csv.reader(open(filename,'r'))
    for rec in f:
        ls=['Age','Sedentary', 'Moderately Active', 'Active']
        row=dict(zip(ls,rec))
        if int(row['Age'])==age: recommcal=int(row[Lifestyle])
    return recommcal,Lifestyle
#START OF THE MAIN PROGRAM
#DICTIONARY CONTAINING the CALORIES and OPTIONS 
Options={'A':200,'B':240,'C':280,'D':320,'E':360,'F':400,'G':440,'H':480,'I':520,'J':560,'K':600,'L':640}
breakfastcalories=totalcals=0
count=5
ch=True
while ch!=0 and count>0:
    print('''=========================MAIN MENU=======================
        

                                                        Welcome to Counting Calories!

                                                        1. START (PART 1)
                                                        2. INSTRUCTIONS
                                                        3. ABOUT
                                                        0. EXIT
                                                            
=========================================================''')
    ch=input('Enter a Choice: ')
    if ch==1:
        name=Name()
        age=Age()
        gender=Gender()
        breakfastitems,bcal=BreakfastMenu(Options)
        lunchitems,lcal=LunchMenu(Options)
        dinneritems,dcal=DinnerMenu(Options)
        Dessertitems,descal=DessertMenu(Options)
        Snackitems,scal=SnackMenu(Options)
        totalcals=bcal+lcal+dcal+descal+scal
        #OPENING THE CORRECT CSV FILE BASED ON USERS GENDER
        if Gender=='M': filename='Male-recomm cals.csv'
        else:filename='Female-recomm cals.csv'
        recommcals=MainMenuPart2(name,filename, age, gender)
        #SUMMARY PAGE END OF PROGRAM
        print' ================================RESULTS SUMMARY========================\n'
        print'\t\t\tLIFESTYLE CATEGORIES:',' \n'

        print '''\t\t\tSEDENTARY: 0-8 POINTS'''
        print '''\t\t\tMODERATELY ACTIVE: 9-12 POINTS'''
        print '''\t\t\tACTIVE: 12-15 POINTS'''

        print '\tTotal Calorie intake:', totalcals
        print '\tReccomended Calorie Intake:', recommcals[0][0],'calories','\n'
        print '\tLifestyle: ',recommcals[0][1]
        print '\tScore: ',recommcals[1]

        print '\tYOUR DIET:'
        for breakfast in breakfastitems:
            print '\t',breakfast
        for lunch in lunchitems:
            print '\t',lunch
        for dinner in dinneritems:
            print '\t',dinner
        for dessert in Dessertitems:
            print '\t',dessert
        for snack in Snackitems:
            print '\t',snack
        
        print'============================================================================'
    elif ch==2:
        print('''======================INSTRUCTIONS=======================


        How Part 1 Works:
        
        1. Enter your personal details
        2. Enter your meal selection from our set menus
        3. Move onto part2!


============================================================ ''')
    elif ch==3:
        print('''==========================ABOUT==========================


         Message from the Author:
        
         The Counting Calories programme uses age,gender and calorie data,
         to calculate whether you're consuming the reccomended calories.




==================================================================''')
    elif str(ch) not in "0123":
        count-=1
        print '\nINVALID ENTRY.\nAttempts Remaining:',count
        if count==0:
            time.sleep(1)
            print 'Goodbye...'
            
            
        
    



    


    
    




