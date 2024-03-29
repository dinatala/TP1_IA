def Moyenne():
 
  note1=int(input("enter a value for note 1:"))
  note2=int(input("enter a value for note 2:"))
  note3=int(input("enter a value for note 3:"))
  m =(note1 +note2 +note3)/3

  if m>=16:
      print("le moyenne" +str(m)+"est très bien") 
  elif 14<m<16:    
      print("le moyenne "+str(m)+"est bien")   
  elif 12<m<14:    
      print("le moyenne" +str(m)+ "est passable")   
  else:
      print("le moyenne" +str(m)+ "est insuffisant")
            
Moyenne() 