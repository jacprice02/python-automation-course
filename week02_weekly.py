def day8():
   def initials_remover(full_name):
        full_name = full_name.strip()
        names = full_name.split() 
        initials = ""
        number_of_letters = 0
        for name in names:
           initials += name[0].upper()
           for letter in name:
              if letter.isalpha():
               number_of_letters += 1
        return(f"{initials} , {number_of_letters}")
      
        

    
   print(initials_remover("Jacob Price"))
def day9():
 def list_value_reporter(scores):
   number_of_values = 0
   sum_of_scores = 0  
   if not scores:
      print("There are no values in the list")
      return
   else:
      for i in scores:
        if isinstance(i,int) or isinstance(i,float):
         highest_score = i
         lowest_score = i
         break
      scores_above = 0   
      for score in scores:   
        if isinstance(score,int) or isinstance(score,float):
           number_of_values += 1
           sum_of_scores += score
           
           if highest_score < score:
             highest_score = score
           if lowest_score > score:
             lowest_score = score 
           if score > 10:
             scores_above += 1            
   if number_of_values == 0:
         print("No numerical Values")
         return
   average = (sum_of_scores/number_of_values)
   rounded_average = round(average , 2)
   print(f"The average is {rounded_average}\nThe highest score is {highest_score}\nThe Lowest score is {lowest_score}\nThere are {scores_above} scores above 10  ")       
   
 list_value_reporter(["yo","hi"])
















day9()