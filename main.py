from data import question_data
from question_model import Question 
from quiz_brain import Quiz_Brain

question_bank=[]
for i in range(len(question_data)):
    name = Question(question_data[i]["text"],question_data[i]["answer"])
    question_bank.append(name)
print(question_bank[0].question)

quiz_brain = Quiz_Brain(question_list=question_bank)
while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("Congrats, you have completed the quiz")
print("Your final score is ",str(quiz_brain.score)+"/"+str(quiz_brain.question_number))