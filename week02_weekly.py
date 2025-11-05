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

day8()
