print "Welcome to the Wedding Guest List Planner!"

score = 0

def main():
	start_quiz= raw_input('Would you like to rate a prospective guest? Y/N')
	starting_quiz= start_quiz.upper()
	if starting_quiz== "Y":
		guest= raw_input("Please enter the name of your prospective guest.")

		print "Thank you. Now let's start the questionnaire."

		q1= int(raw_input("Have you spoken to this person within the last two years? Enter 1 for YES or 2 for NO"))
		global score
		if q1==1:
			score= score +1
			score 
		else:
			score= score +0

		q2= int(raw_input("Are you aware of the day-to-day aspects of this person's life? Enter 1 for YES or 2 for NO or 3 for MODERATELY"))
		if q2==1:
			score= score +2
			score 
		elif q2==3:
			score= score+1
		else:
			score= score +0
	
		q3= int(raw_input("Would you be offended not receiving an invite to their wedding? Enter 1 for YES or 2 for NO or 3 for MODERATELY"))
		if q3==1:
			score= score +2
			score
		elif q3==3:
			score= score+1
		else:
			score= score +0

		q4= int(raw_input("Do you spend birthdays and other celebrations with this person? Enter 1 for YES or 2 for NO or 3 for MODERATELY"))
		if q4==1:
			score= score +2
			score 
		elif q4==3:
			score= score+1
		else:
			score= score +0

		q5= int(raw_input("Will you be inviting several members of their family? Enter 1 for YES or 2 for NO"))
		if q5==1:
			score= score +1
			score 
		else:
			score= score +0

		q6= int(raw_input("Is this person a positive influence in your life? Enter 1 for YES or 2 for NO or 3 for MODERATELY"))
		if q6==1:
			score= score +2
			score 
		elif q6==3:
			score= score+1
		else:
			score= score +0

		q7= int(raw_input("If you moved away, would you keep in touch? Enter 1 for YES or 2 for NO"))
		if q7==1:
			score= score +1
			extra_q7= int(raw_input("If we were in town, would you call them ahead of time to let them know? Enter 1 for YES or 2 for NO"))
			if extra_q7==1:
				score= score +1
			else:
				score= score+ 0
			score 
		else:
			score= score +0

		q8= int(raw_input("Would you change the date of your wedding if this person couldn't come? Enter 1 for YES or 2 for NO or 3 for MAYBE"))
		if q8==1:
			score= score +2
			score
		elif q8==3:
			score= score+1
		else:
			score= score +0
	else:
		exit()

	print guest +"'s total score is", score


while True:
	main()
else:
	exit()
