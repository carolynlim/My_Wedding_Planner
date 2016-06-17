score = 0
guest= None
guest_list= {}
print "Welcome to the wedding guestlist scorecard!"

def prompt_user():
	global guest
	guest= raw_input("Please enter the name of your prospective guest \n")
	
def question1():
	global score
	q1= int(raw_input("Have you spoken to this person within the last two years? \n Enter 1 for YES \n Enter 2 for NO \n"))
	if q1==1:
		score= score +10
		score 
	elif q1==2:
		score= score +5
	else:
		print "Please enter valid answer"
		question1()

def question2():
	global score
	q2= int(raw_input("Are you aware of the day-to-day aspects of this person's life? \n Enter 1 for YES \n Enter 2 for NO \n Enter 3 for MODERATELY \n"))
	if q2==1:
		score= score +10
		score 
	elif q2==3:
		score= score+9
	elif q2==2:
		score= score +5
	else:
		print "Please enter valid answer"
		question2()

def question3():
	global score
	q3= int(raw_input("Would you be offended not receiving an invite to their wedding? \n Enter 1 for YES \n Enter 2 for NO \n Enter 3 for MODERATELY \n"))
	if q3==1:
		score= score +15
		score
	elif q3==3:
		score= score+14
	elif q3==2:
		score= score +5
	else:
		print "Please enter valid answer"
		question3()

def question4():
	global score
	q4= int(raw_input("Do you spend birthdays and other celebrations with this person? \n Enter 1 for YES \n Enter 2 for NO \n Enter 3 for MODERATELY \n"))
	if q4==1:
		score= score +10
		score 
	elif q4==3:
		score= score+9
	elif q4==2:
		score= score +5
	else:
		print "Please enter valid answer"
		question4()

def question5():
	global score
	q5= int(raw_input("Will you be inviting several members of their family? \n Enter 1 for YES \n Enter 2 for NO \n"))
	if q5==1:
		score= score +10
		score 
	elif q5==2:
		score= score +5
	else:
		print "Please enter valid answer"
		question5()

def question6():
	global score
	q6= int(raw_input("Is this person a positive influence in your life? \n Enter 1 for YES \n Enter 2 for NO \n Enter 3 for MODERATELY \n"))
	if q6==1:
		score= score +10
		score 
	elif q6==3:
		score= score+9
	elif q6==2:
		score= score +5
	else:
		print "Please enter valid answer"
		question6()

def question7():
	global score
	q7= int(raw_input("If you moved away, would you keep in touch? \n Enter 1 for YES \n Enter 2 for NO \n"))
	if q7==1:
		score= score +15
		extra_q7= int(raw_input("If we were in town, would you call them ahead of time to let them know? \n Enter 1 for YES \n Enter 2 for NO \n"))
		if extra_q7==1:
			score= score +10
		else:
			score= score +9
		score 
	elif q7==2:
		score= score +5
	else:
		print "Please enter valid answer"
		question7()

def question8():
	global score
	q8= int(raw_input("Would you change the date of your wedding if this person couldn't come? \n Enter 1 for YES \n Enter 2 for NO \n Enter 3 for MAYBE \n"))
	if q8==1:
		score= score +10
		score
	elif q8==3:
		score= score+9
	elif q8==2:
		score= score +5
	else:
		print "Please enter valid answer"
		question8()

def main():
	
	prompt_user()
	question1()
	question2()
	question3()
	question4()
	question5()
	question6()
	question7()
	question8()

	print guest +"'s total score is", score


if __name__ == '__main__':
    main()

while True:
	guest_list[guest]= score
	start_quiz= raw_input("Would you like to rate another guest? Y/N \n")
	starting_quiz= start_quiz.upper()
	if starting_quiz== "Y":
		score = 0
		main()
	else:
		print "Your guestlist has been populated in the wedding guestlist text file \n"
		with open("wedding_guestlist.txt", 'w') as f:
			for key,value in guest_list.items():
				if value >= 80:
					f.write('%s\n' % (key))
		exit()