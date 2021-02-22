class Quiz_Brain:
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
    
    def check_answer(self,user_given,answer):
        true_list = ['True', 't','Truthy','Y','y']
        false_list = ['False','f','Falsey','N','n']
        if answer == "True":
            if user_given in true_list:
                print("Correct,answer is ",answer)
                self.score +=1
            else:
                print("Incorrect, correct answer is ",answer)
        elif answer == "False":
            if user_given in false_list:
                print("Correct,answer is ",answer)
                self.score +=1
            else:
                print("Incorrect, correct answer is ",answer)
        else:
            print("Invalid input")

    
    def next_question(self):
        
        current_question = self.question_number
        self.question_number +=1
        question = self.question_list[current_question].question 
        options = "True/False"
        answer = self.question_list[current_question].answer
        user_given = input("Q."+str(self.question_number)+" "+question+" "+options+"? :")
        self.check_answer(user_given,answer)
        print("Your current score is "+ str(self.score)+"/"+str(self.question_number))


    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            False

   
            


            
    