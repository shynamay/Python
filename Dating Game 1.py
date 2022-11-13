import time

def Hobbies():
  print("Choose hobbies/Interest that you have in common with you") 
  print("Music, Anime, Novel Books")
  topic = input()
  if topic == "Music":
    print()
    print("Yey! You've matched with people who share your interests.")
    print()
    Music()
  elif topic == "Anime":
    print()
    print("Yey! You've matched with people who share your interests.")
    print()
    Anime()
  elif topic == "Novel Books":
    print()
    print("Yey! You've matched with people who share your interests.")
    print()
    NovelBooks()
    
print()

def Music():
  print("Choose which genre your interested in.")
  print("POP, BedroomPOP, ElectroPOP")
  subtopic = input()
  if subtopic == "POP":
    print()
    print("Yehey! You've matched with people who loves music.")
    print()
    POP()
  elif subtopic == "BedroomPOP":
    print()
    print("Yehey! You've matched with people who loves music.")
    print()
    BedroomPOP()
  elif subtopic == "ElectroPOP":
    print()
    print("Yehey! You've matched with people who loves music.")
    print()
    ElectroPOP()

print()

def POP():
  print("Here are you matched with")
  print("Taylor, Harry, Bruno")
  peepk = input()
  if peepk == "Taylor":
    print()
    print("Congratulations, you've got a date!")
    print()
    Taylor()
  elif peepk == "Harry":
    print()
    print("Congratulations, you've got a date!")
    print()
    Gracie() 
  elif peepk == "Bruno":
    print()
    print("Congratulations, you've got a date!")
    print()
    Bruno()

print()

def BedroomPOP():
  print("Here are you matched with")
  print("Clairo, Gracie, GirlInRed")
  peepk = input()
  if peepk == "Clairo":
    print()
    print("Congratulations, you've got a date!")
    print()    
    Clairo()
  elif peepk == "Gracie":
    print()
    print("Congratulations, you've got a date!")
    print()
    Gracie()
  elif peepk == "GirlInRed":
    print()
    print("Congratulations, you've got a date!")  
    print()
    GirlInRed() 



print()

def ElectroPOP():
  print("Here are you matched with")
  print("Billie, Britney, Lady")
  peepk = input()
  if peepk == "Billie":
    print()
    print("Congratulations, you've got a date!")
    print()
    Billie()
  elif peepk == "Lady":
    print()
    print("Congratulations, you've got a date!")
    print()
    Lady()
  elif peepk == "Britney":
    print()
    print("Congratulations, you've got a date!")
    print()
    Britney()


print()

def Taylor():
  print("Do you want to know about Taylor?") 
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Heres his/her Status ")
  time.sleep(3)
  print()
  print("Taylor's Status/Bio")
  print("Real Name: Taylor Alison Swift")
  print("Born: December 13, 1989 (Age 32) West Reading, Pennsylvania, U.S. ")
  print("Her other Genres: Pop, Country, Folk, Rock, Alternative")
  print("Occupation: Singer-songwriter, Producer, Director, Actress, Businesswoman")
  print("Works: Albums, Singles, Songs, Performances, Videography")
  print()
  if swipea == "No":
    print("No I don't want to.")
  time.sleep(3)
  print("Do you want to Taylor to be your date?")
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Congratulations! You have been matched with Taylor.")
  elif swipea == "No":
      print("I want someone else")
  time.sleep(3)
  print()
  print("Do you want to Play Again")
  print("Enter y/n")
  swipea = input()
  if swipea == "y":
    print("Welcome to Dating Game")
    print()
    Hobbies()
  while swipea == "n":
    print("Thank You for Playing")
    break
    Hobbies()

print()

def Harry():
  print("Do you want to know about Harry?") 
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Heres his/her Status ")
  time.sleep(3)
  print()
  print("Harry's Status/Bio")
  print("Real Name: Harry Edward Styles")
  print("Born: 1 February 1994 (age 28) Redditch, England")
  print("Occupation: Singer, SongWriter, Actor")
  print("Works:	Solo discography[a]songs written")
  print("Here other Genres: Popsoft, Rock")
  print()
  if swipea == "No":
    print("No I don't want to.")
  time.sleep(3)
  print("Do you want to Harry to be your date?")
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Congratulations! You have been matched with Harry.")
  elif swipea == "No":
      print("I want someone else")
  time.sleep(3)
  print()
  print("Do you want to Play Again")
  print("Enter y/n")
  swipea = input()
  if swipea == "y":
    print("Welcome to Dating Game")
    print()
    Hobbies()
  while swipea == "n":
    print("Thank You for Playing")
    break
    Hobbies()

print()

def Bruno():
  print("Do you want to know about Bruno?") 
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Heres his/her Status ")
  time.sleep(3)
  print()
  print("Bruno's Status/Bio")
  print("Real Name: Bruno Major")
  print("Born: 15 July 1988 (age 34) Northampton, England")
  print("His other Genres:R&B, Pop")
  print("Occupation(s):	Singer-songwriter")
  print()
  if swipea == "No":
    print("No I don't want to.")
  time.sleep(3)
  print("Do you want to Bruno to be your date?")
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Congratulations! You have been matched with Bruno.")
  elif swipea == "No":
      print("I want someone else")
  time.sleep(3)
  print()
  print("Do you want to Play Again")
  print("Enter y/n")
  swipea = input()
  if swipea == "y":
    print("Welcome to Dating Game")
    print()
    Hobbies()
  while swipea == "n":
    print("Thank You for Playing")
    break
    Hobbies()

print()

def Clairo():
  print("Do you want to know about Clairo?") 
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Heres his/her Status ")
  time.sleep(3)
  print()
  print("Clairo's Status/Bio")
  print("Real Name: Claire Elizabeth Cottrill")
  print("Born: August 18, 1998 (age 24)[1] Atlanta, Georgia, U.S. ")
  print("Occupation(s):	Singer-songwriter")
  print()
  if swipea == "No":
    print("No I don't want to.")
  time.sleep(3)
  print("Do you want to Clairo to be your date?")
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Congratulations! You have been matched with Clairo.")
  elif swipea == "No":
      print("I want someone else")
  time.sleep(3)
  print()
  print("Do you want to Play Again")
  print("Enter y/n")
  swipea = input()
  if swipea == "y":
    print("Welcome to Dating Game")
    print()
    Hobbies()
  while swipea == "n":
    print("Thank You for Playing")
    break
    Hobbies()

print()

def GirlInRed():
  print("Do you want to know about GilrInRed?") 
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Heres his/her Status ")
  time.sleep(3)
  print()
  print("GirlInRed's Status/Bio")
  print("Real Name: Marie Ulven Ringheim")
  print("Born: 16 February 1999 (age 23) Horten, Norway")
  print("Occupation(s):	Singer-songwriter, music producer")
  print()
  if swipea == "No":
    print("No I don't want to.")
  time.sleep(3)
  print("Do you want to GirlInRed to be your date?")
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Congratulations! You have been matched with GirlInRed.")
  elif swipea == "No":
      print("I want someone else")
  time.sleep(3)
  print()
  print("Do you want to Play Again")
  print("Enter y/n")
  swipea = input()
  if swipea == "y":
    print("Welcome to Dating Game")
    print()
    Hobbies()
  while swipea == "n":
    print("Thank You for Playing")
    break
    Hobbies()

print()

def Gracie():
  print("Do you want to know about Gracie?") 
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Heres his/her Status ")
  time.sleep(3)
  print()
  print("Gracie's Status/Bio")
  print("Real Name: Gracie Madigan Abrams")
  print("Born: September 7, 1999 (Age 23) Los Angeles, California, U.S.")
  print("Alma mater: Barnard College")
  print("Occupation: Singer, songwriter")
  print()
  if swipea == "No":
    print("No I don't want to.")
  time.sleep(3)
  print("Do you want to Gracie to be your date?")
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Congratulations! You have been matched with Gracie.")
  elif swipea == "No":
      print("I want someone else")
  time.sleep(3)
  print()
  print("Do you want to Play Again")
  print("Enter y/n")
  swipea = input()
  if swipea == "y":
    print("Welcome to Dating Game")
    print()
    Hobbies()
  while swipea == "n":
    print("Thank You for Playing")
    break
    Hobbies()

print()

def Billie():
  print("Do you want to know about Billie?") 
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Heres his/her Status ")
  time.sleep(3)
  print()
  print("Billie's Status/Bio")
  print("Real Name: Billie Eilish Pirate Baird O'Connell")
  print("Born: December 18, 2001 (age 20) Los Angeles, California, U.S. ")
  print("Occupation: Singer, Songwriter")
  print("Works:	Discography, Songs recorded ")
  print("Her other Genres: Pop, alt-pop, Electro Pop")
  print()
  if swipea == "No":
    print("No I don't want to.")
  time.sleep(3)
  print("Do you want to Billie to be your date?")
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Congratulations! You have been matched with Billie.")
  elif swipea == "No":
      print("I want someone else")
  time.sleep(3)
  print()
  print("Do you want to Play Again")
  print("Enter y/n")
  swipea = input()
  if swipea == "y":
    print("Welcome to Dating Game")
    print()
    Hobbies()
  while swipea == "n":
    print("Thank You for Playing")
    break
    Hobbies()

print()

def Lady():
  print("Do you want to know about Lady?") 
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Heres his/her Status ")
  time.sleep(3)
  print()
  print("Lady's Status/Bio")
  print("Real Name: Stefani Joanne Angelina Germanotta aka Lady Gaga")
  print("March 28, 1986 (age 36) New York City, U.S. ")
  print("Ocuupation(s): Singer,Songwriter, Actress")
  print("Work: Discography, Songs, Videography, Performances")
  print()
  if swipea == "No":
    print("No I don't want to.")
  time.sleep(3)
  print("Do you want to Lady to be your date?")
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Congratulations! You have been matched with Lady.")
  elif swipea == "No":
      print("I want someone else")
  time.sleep(3)
  print()
  print("Do you want to Play Again")
  print("Enter y/n")
  swipea = input()
  if swipea == "y":
    print("Welcome to Dating Game")
    print()
    Hobbies()
  while swipea == "n":
    print("Thank You for Playing")
    break
    Hobbies()

print()

def Britney():
  print("Do you want to know about Britney?") 
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Heres his/her Status ")
  time.sleep(3)
  print()
  print("Britney's Status/Bio")
  print("Real Name: Britney Jean Spears")
  print("Born: December 2, 1981 (age 40) McComb, Mississippi, U.S.")
  print("Education: Professional Performing Arts School Parklane Academy[")
  print("Occupation: Singer, Songwriter, Dance, Actress")
  print("Works: Discography, Songs, Videography")
  print()
  if swipea == "No":
    print("No I don't want to.")
  time.sleep(3)
  print("Do you want to Britney to be your date?")
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Congratulations! You have been matched with Britney.")
  elif swipea == "No":
      print("I want someone else")
  time.sleep(3)
  print()
  print("Do you want to Play Again")
  print("Enter y/n")
  swipea = input()
  if swipea == "y":
    print("Welcome to Dating Game")
    print()
    Hobbies()
  while swipea == "n":
    print("Thank You for Playing")
    break
    Hobbies()

print()

def Anime():
  print("Choose what favorite animes you like.")
  print("One Piece, Bleach, Naruto")
  animes = input()
  if animes == "Bleach":
    print()
    print("Yey! You've matched with people who loves to watched Anime.")
    print()
    Bleach()
  elif animes == "One Piece":
    print()
    print("Yey! You've matched with people who loves to watched Anime.")
    print()
    OnePiece()
  elif animes == "Naruto":
    print()
    print("Yey! You've matched with people who loves to watched Anime.")
    print()
    Naruto()

print()

def Naruto():
  print("You have been paired with")
  print("Sakura, Hinata, Sasuke")
  peepks = input()
  if peepks == "Sakura":
    print()
    print("Congratulations, you've got a date!")
    print()
    Sakura()
  elif peepks == "Sasuke":
    print()
    print("Congratulations, you've got a date!")
    print()
    Sasuke()
  elif peepks == "Hinata":
    print()
    print("Congratulations, you've got a date!")
    print()
    Hinata() 

print()

def Bleach():
  print("You have been paired with")
  print("Ichigo, Aizen, Renji")
  peepks = input()
  if peepks == "Aizen":
    print()
    print("Congratulations, you've got a date!")
    print()
    Aizen()
  elif peepks == "Ichigo":
    print()
    print("Congratulations, you've got a date!")
    print()
    Ichigo()
  elif peepks == "Renji":
    print()
    print("Congratulations, you've got a date!")
    print()
    Renji() 

print()

def OnePiece():
  print("You have been paired with")
  print("Sanji, Luffy, Zoro")
  peepks = input()
  if peepks == "Luffy":
    print()
    print("Congratulations, you've got a date!")
    print()
    Luffy()
  elif peepks == "Zoro":
    print()    
    print("Congratulations, you've got a date!")
    print()
    Zoro()
  elif peepks == "Sanji":
    print()
    print("Congratulations, you've got a date!")
    print()
    Sanji()
 
print()

def Sakura():
  print("Do you want to know about Sakura?") 
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Heres his/her Status ")
  time.sleep(3)
  print()
  print("Sakura's Status/Bio")
  print("Real Name: Sakura Haruno")
  print("Born: Konoha, March 28 (18 years old)")
  print("Height: 165 cm")
  print("BloodType: O")
  print("He loves Watching Naruto")
  print()
  if swipea == "No":
    print("No I don't want to.")
  time.sleep(3)
  print("Do you want to Sakura to be your date?")
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Congratulations! You have been matched with Sakura.")
  elif swipea == "No":
      print("I want someone else")
  time.sleep(3)
  print()
  print("Do you want to Play Again")
  print("Enter y/n")
  swipea = input()
  if swipea == "y":
    print("Welcome to Dating Game")
    print()
    Hobbies()
  while swipea == "n":
    print("Thank You for Playing")
    break
    Hobbies()


print()

def Sasuke():
  print("Do you want to know about Sasuke?") 
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Heres his/her Status ")
  time.sleep(3)
  print()
  print("Sasuke's Status/Bio")
  print("Real Name: Sasuke Uchicha")
  print("Born: Konoha, July 23th (19 years old)")
  print("He loves Watching Naruto")
  print()
  if swipea == "No":
    print("No I don't want to.")
  time.sleep(3)
  print("Do you want to Sakura to be your date?")
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Congratulations! You have been matched with Sakura.")
  elif swipea == "No":
      print("I want someone else")
  time.sleep(3)
  print()
  print("Do you want to Play Again")
  print("Enter y/n")
  swipea = input()
  if swipea == "y":
    print("Welcome to Dating Game")
    print()
    Hobbies()
  while swipea == "n":
    print("Thank You for Playing")
    break
    Hobbies()

print()

def Hinata():
  print("Do you want to know about Hinata?") 
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Heres his/her Status ")
  time.sleep(3)
  print()
  print("Hinata's Status/Bio")
  print("Real Name: Hinata Hyuga")
  print("Born: Konoha, December 27 (18 years old)")
  print("Height: 163 cm")
  print("Blood type: A")
  print("He loves Watching Naruto")
  print()
  if swipea == "No":
    print("No I don't want to.")
  time.sleep(3)
  print("Do you want to Hinata to be your date?")
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Congratulations! You have been matched with Hinata.")
  elif swipea == "No":
      print("I want someone else")
  time.sleep(3)
  print()
  print("Do you want to Play Again")
  print("Enter y/n")
  swipea = input()
  if swipea == "y":
    print("Welcome to Dating Game")
    print()
    Hobbies()
  while swipea == "n":
    print("Thank You for Playing")
    break
    Hobbies()

print()

def Aizen():
  print("Do you want to know about Aizen?") 
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Heres his/her Status ")
  time.sleep(3)
  print()
  print("Aizen's Status/Bio")
  print("Real Name: Sōsuke Aizen")
  print("Height: 186 cm (6'1)")
  print("Birthdate: May 29th (29 years old)")
  print("He loves Watching Bleach")
  print()
  if swipea == "No":
    print("No I don't want to.")
  time.sleep(3)
  print("Do you want to Aizen to be your date?")
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Congratulations! You have been matched with Aizen.")
  elif swipea == "No":
      print("I want someone else")
  time.sleep(3)
  print()
  print("Do you want to Play Again")
  print("Enter y/n")
  swipea = input()
  if swipea == "y":
    print("Welcome to Dating Game")
    print()
    Hobbies()
  while swipea == "n":
    print("Thank You for Playing")
    break
    Hobbies()

print()

def Ichigo():
  print("Do you want to know about Ichigo?") 
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Heres his/her Status ")
  time.sleep(3)
  print()
  print("Ichigo's Status/Bio")
  print("Real Name: Ichigo Kurosaki")
  print("Height: 181 cm (5'11¼)")
  print("Birthdate: July 15 (Cancer) (27 years old")
  print("He loves Watching Bleach")
  print()
  if swipea == "No":
    print("No I don't want to.")
  time.sleep(3)
  print("Do you want to Ichigo to be your date?")
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Congratulations! You have been matched with Ichigo.")
  elif swipea == "No":
      print("I want someone else")
  time.sleep(3)
  print()
  print("Do you want to Play Again")
  print("Enter y/n")
  swipea = input()
  if swipea == "y":
    print("Welcome to Dating Game")
    print()
    Hobbies()
  while swipea == "n":
    print("Thank You for Playing")
    break
    Hobbies()


print()

def Renji():
  print("Do you want to know about Renji?") 
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Heres his/her Status ")
  time.sleep(3)
  print()
  print("Renji's Status/Bio")
  print("Real Name: Renji Abarai")
  print("Height: ")
  print("Birthdate: 188 cm (6'2) (29 years old)")
  print("He loves Watching Bleach")
  print()
  if swipea == "No":
    print("No I don't want to.")
  time.sleep(3)
  print("Do you want to Renji to be your date?")
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Congratulations! You have been matched with Renji.")
  elif swipea == "No":
      print("I want someone else")
  time.sleep(3)
  print()
  print("Do you want to Play Again")
  print("Enter y/n")
  swipea = input()
  if swipea == "y":
    print("Welcome to Dating Game")
    print()
    Hobbies()
  while swipea == "n":
    print("Thank You for Playing")
    break
    Hobbies()

print()

def Luffy():
  print("Do you want to know about Luffy?") 
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Heres his/her Status ")
  time.sleep(3)
  print()
  print("Luffy's Status/Bio")
  print("Real Name: Monkey D. Luffy")
  print("Height: 174 cm (5'8½)")
  print("Birthdate: May 5th (19 years old)")
  print("He loves Watching One Piece")
  print()
  if swipea == "No":
    print("No I don't want to.")
  time.sleep(3)
  print("Do you want to Luffy to be your date?")
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Congratulations! You have been matched with Luffy.")
  elif swipea == "No":
      print("I want someone else")
  time.sleep(3)
  print()
  print("Do you want to Play Again")
  print("Enter y/n")
  swipea = input()
  if swipea == "y":
    print("Welcome to Dating Game")
    print()
    Hobbies()
  while swipea == "n":
    print("Thank You for Playing")
    break
    Hobbies()

print()

def Zoro():
  print("Do you want to know about Zoro?") 
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Heres his/her Status ")
  time.sleep(3)
  print()
  print("Zoro's Status/Bio")
  print("Real Name: Roronoa Zoro ")
  print("Height: 181 cm (5'11⅝)")
  print("Birthdate: November 11th (21y years old)")
  print("He loves Watching One Piece")
  print()
  if swipea == "No":
    print("No I don't want to.")
  time.sleep(3) 
  print("Do you want to Zoro to be your date?")
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Congratulations! You have been matched with Zoro.")
  elif swipea == "No":
      print("I want someone else")
  time.sleep(3)
  print()
  print("Do you want to Play Again")
  print("Enter y/n")
  swipea = input()
  if swipea == "y":
    print("Welcome to Dating Game")
    print()
    Hobbies()
  while swipea == "n":
    print("Thank You for Playing")
    break
    Hobbies()

print()

def Sanji():
  print("Do you want to know about Sanji?") 
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Heres his/her Status ")
  time.sleep(3)
  print()
  print("Sanji's Status/Bio")
  print("Real Name: Vinsmoke Sanji ")
  print("Height: 180 cm (5'11¾) ")
  print("Birthdate: March 2nd (21y years old)")
  print("He loves Watching One Piece")
  print()
  if swipea == "No":
    print("No I don't want to.")
  time.sleep(3) 
  print("Do you want to Sanji to be your date?")
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Congratulations! You have been matched with Sanji.")
  elif swipea == "No":
      print("I want someone else")
  time.sleep(3)
  print()
  print("Do you want to Play Again")
  print("Enter y/n")
  swipea = input()
  if swipea == "y":
    print("Welcome to Dating Game")
    print()
    Hobbies()
  while swipea == "n":
    print("Thank You for Playing")
    break
    Hobbies()

print()


def NovelBooks():
  print("Choose which genre book your interested in.")
  print("Action, Mystery, SciFic")
  bookd = input()
  if bookd == "Action":
    print()
    print("Yehey! You've matched with people who same interest genre you read.")
    print()
    Action()
  elif bookd == "Mystery":
    print()
    print("Yehey! You've matched with people who same interest genre you read.")
    print()
    Mystery()
  elif bookd == "SciFic":
    print()
    print("Yehey! You've matched with people who same interest genre you read.")
    print()
    SciFic()
   
print()

def Action():
  print("Here are you matched with")
  print("Alladin, Alibaba, Sinbad")
  peepk = input()
  if peepk == "Alladin":
    print()
    print("Congratulations, you've got a date!")
    print()
    Alladin()
  elif peepk == "Alibaba":
    print()
    print("Congratulations, you've got a date!")
    print()
    Alibaba() 
  elif peepk == "Sinbad":
    print()
    print("Congratulations, you've got a date!")
    print()
    Sinbad()
 
print()

def Mystery():
  print("Here are you matched with")
  print("Sawako, Kazehaya, Ryu")
  peepk = input()
  if peepk == "Sawako":
    print()
    print("Congratulations, you've got a date!")
    print()
    Sawako()
  elif peepk == "Ryu":
    print()
    print("Congratulations, you've got a date!")
    print()
    Ryu()
  elif peepk == "Kazehaya":
    print()
    print("Congratulations, you've got a date!")
    print()
    Kazehaya()
 
print()

def SciFic():
  print("Here are you matched with")
  print("Kageyama, Yamaguchi, Tsukishima")
  peepk = input()
  if peepk == "Tsukishma":
    print()
    print("Congratulations, you've got a date!")
    print()
    Tsukishima()
  elif peepk == "Yamaguchi":
    print()
    print("Congratulations, you've got a date!")
    print()
    Yamaguchi()
  elif peepk == "Kageyama":
    print()
    print("Congratulations, you've got a date!")
    print()
    Kageyama() 
 
print()

def Alladin():
  print("Do you want to know about Alladin?") 
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Heres his/her Status ")
  time.sleep(3)
  print()
  print("Alladin's Status/Bio")
  print("Age: 18 years old")
  print("Height: 167 cm (5'5)")
  print("Weight: 36 kg (79 lbs)")
  print("He loves to read Fantasy genre novel books")
  print()
  if swipea == "No":
    print("No I don't want to.")
  time.sleep(3) 
  print("Do you want to Alladin to be your date?")
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Congratulations! You have been matched with Alladin.")
  elif swipea == "No":
      print("I want someone else")
  time.sleep(3)
  print()
  print("Do you want to Play Again")
  print("Enter y/n")
  swipea = input()
  if swipea == "y":
    print("Welcome to Dating Game")
    print()
    Hobbies()
  while swipea == "n":
    print("Thank You for Playing")
    break
    Hobbies()

print()

def Alibaba():
  print("Do you want to know about Alibaba?") 
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Heres his/her Status ")
  time.sleep(3)
  print()
  print("Alibaba's Status/Bio")
  print("Real Name: Alibaba Saluja")
  print("Age: 22 years old")
  print("Height: 170 cm (5'7)")
  print("Weight: 64 kg (141 lbs)")
  print("He loves to read Fantasy genre novel books")
  print()
  if swipea == "No":
    print("No I don't want to.")
  time.sleep(3) 
  print("Do you want to Alibaba to be your date?")
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Congratulations! You have been matched with Alibaba.")
  elif swipea == "No":
      print("I want someone else")
  time.sleep(3)
  print()
  print("Do you want to Play Again")
  print("Enter y/n")
  swipea = input()
  if swipea == "y":
    print("Welcome to Dating Game")
    print()
    Hobbies()
  while swipea == "n":
    print("Thank You for Playing")
    break
    Hobbies()

print()

def Sinbad():
  print("Do you want to know about Sinbad?") 
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Heres his/her Status ")
  time.sleep(3)
  print()
  print("Sinbad's Status/Bio")
  print("Age: 30 years old")
  print("Height: 183 cm (6'0)")
  print("Weight: 83 kg (183 lbs)")
  print("He loves to read Action genre novel books")
  print()
  if swipea == "No":
    print("No I don't want to.")
  time.sleep(3) 
  print("Do you want to Sinbad to be your date?")
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Congratulations! You have been matched with Sinbad.")
  elif swipea == "No":
      print("I want someone else")
  time.sleep(3)
  print()
  print("Do you want to Play Again")
  print("Enter y/n")
  swipea = input()
  if swipea == "y":
    print("Welcome to Dating Game")
    print()
    Hobbies()
  while swipea == "n":
    print("Thank You for Playing")
    break
    Hobbies()

print()

def Sawako():
  print("Do you want to know about Sawako?") 
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Heres his/her Status ")
  time.sleep(3)
  print()
  print("Sawako's Status/Bio")
  print("Real Name: Kuronuma Sawako")
  print("Motto: One good deed per day.")
  print("Birthdate: December 31 (18 years old)")
  print("Height: 158 cm (5'2) ")
  print("He loves to read Mystery genre novel books")
  print()
  if swipea == "No":
    print("No I don't want to.")
  time.sleep(3) 
  print("Do you want to Sawako to be your date?")
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Congratulations! You have been matched with Sawako.")
  elif swipea == "No":
      print("I want someone else")
  time.sleep(3)
  print()
  print("Do you want to Play Again")
  print("Enter y/n")
  swipea = input()
  if swipea == "y":
    print("Welcome to Dating Game")
    print()
    Hobbies()
  while swipea == "n":
    print("Thank You for Playing")
    break
    Hobbies()

print()

def Ryu():
  print("Do you want to know about Ryu?") 
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Heres his/her Status ")
  time.sleep(3)
  print()
  print("Ryu's Status/Bio")
  print("Real Name: Sanada Ryū ")
  print("Motto: Work silently")
  print("Birthdate: December 2 (18 years old)")
  print("Height: 179 cm (5'10)")
  print("He loves to read Mystery genre novel books")
  print()
  if swipea == "No":
    print("No I don't want to.")
  time.sleep(3) 
  print("Do you want to Ryu to be your date?")
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Congratulations! You have been matched with Ryu.")
  elif swipea == "No":
      print("I want someone else")
  time.sleep(3)
  print()
  print("Do you want to Play Again")
  print("Enter y/n")
  swipea = input()
  if swipea == "y":
    print("Welcome to Dating Game")
    print()
    Hobbies()
  while swipea == "n":
    print("Thank You for Playing")
    break
    Hobbies()
  

print()

def Kazehaya():
  print("Do you want to know about Kazehaya?") 
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Heres his/her Status ")
  time.sleep(3)
  print()
  print("Kazehaya's Status/Bio")
  print("Real Name: Kazehaya Shōta")
  print("Motto: Believe in and pursue the truth")
  print("Birthdate: May 15 (18 years old)")
  print("Height: 175 cm (5'9)")
  print("He loves to read Mystery genre novel books")
  print()
  if swipea == "No":
    print("No I don't want to.")
  time.sleep(3)
  print("Do you want to Kazehaya to be your date?")
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Congratulations! You have been matched with Kazehaya.")
  elif swipea == "No":
      print("I want someone else")
  time.sleep(3)
  print()
  print("Do you want to Play Again")
  print("Enter y/n")
  swipea = input()
  if swipea == "y":
    print("Welcome to Dating Game")
    print()
    Hobbies()
  while swipea == "n":
    print("Thank You for Playing")
    break
    Hobbies()

print()

def Tsukishima():
  print("Do you want to know about Tsukishima?") 
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Heres his/her Status ")
  time.sleep(3)
  print()
  print("Tsukishima's Status/Bio")
  print("Real Name: Tsukishima Kei")
  print("Goal: Nothing in particular")
  print("Birthdate: September 27, 1996 (26 years old)")
  print("Height: 190.1 cm (6' 2.8)")
  print("He loves to read Sci-Fic genre novel books")
  print()
  if swipea == "No":
    print("No I don't want to.")
  time.sleep(3)
  print("Do you want to Tsukishima to be your date?")
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Congratulations! You have been matched with Tsukishima.")
  elif swipea == "No":
      print("I want someone else")
  time.sleep(3)
  print()
  print("Do you want to Play Again")
  print("Enter y/n")
  swipea = input()
  if swipea == "y":
    print("Welcome to Dating Game")
    print()
    Hobbies()
  while swipea == "n":
    print("Thank You for Playing")
    break
    Hobbies()

print()

def Yamaguchi():
  print("Do you want to know about Yamaguschi?") 
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Heres his/her Status ")
  time.sleep(3)
  print()
  print("Yamaguchi's Status/Bio")
  print("Real Name: Yamaguchi Tadashi")
  print("Goal: Practice more Be able to play in a match as a regular Have a greater presence.")
  print("Birthdate: November 10, 1996 (26 years old)")
  print("Height: 180.0 cm (5' 10.9)")
  print("He loves to read Sci-Fic genre novel books")
  print()
  if swipea == "No":
    print("No I don't want to.")
  time.sleep(3)
  print("Do you want to Yamaguchi to be your date?")
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Congratulations! You have been matched with Yamaguchi.")
  elif swipea == "No":
      print("I want someone else")
  time.sleep(3)
  print()
  print("Do you want to Play Again")
  print("Enter y/n")
  swipea = input()
  if swipea == "y":
    print("Welcome to Dating Game")
    print()
    Hobbies()
  while swipea == "n":
    print("Thank You for Playing")
    break
    Hobbies()

print()

def Kageyama(): 
  print("Do you want to know about Kageyama?") 
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Heres his/her Status ")
  time.sleep(3)
  print()
  print("Kageyama's Status/Bio")
  print("Real Name: Kageyama Tobio")
  print("Goal: Be a setter that's the team's control tower Be able to think and toss the ball in a way so that it won't get blocked.")
  print("Birthdate: December 22, 1996 (26 years old)")
  print("Height: 181.9cm (5' 11.6)")
  print("He loves to read Sci-Fic genre novel books")
  print()
  if swipea == "No":
    print("No I don't want to.")
  time.sleep(3)
  print()
  print("Do you want to Kageyama to be your date?")
  print("Enter Yes/No")
  swipea = input()
  if swipea == "Yes":
    print("Congratulations! You have been matched with Kageyama.")
  elif swipea == "No":
      print("I want someone else")
  time.sleep(3)
  print()
  print("Do you want to Play Again")
  print("Enter y/n")
  swipea = input()
  if swipea == "y":
    print("Welcome to Dating Game")
    print()
    Hobbies()
  while swipea == "n":
    print("Thank You for Playing")
    break
    Hobbies()

if __name__ == "__main__":
  while True:
    print("Welcome to the Dating App Game!")
    print("We want to help lonely people like yourself.")
    print("This Dating App is for those who share your interests and hobbies and want to date.")
    print("Please advance to the game if you are ready.")
    print()
    time.sleep(2)
    print("Please, Enter your name: ")
    name = input() 
    print()
    time.sleep(2)
    print("Please, Enter your age also: ")
    age = input()
    print()
    time.sleep(2)
    print("What is you Sex/Gender?")
    sex = input()
    print()
    time.sleep(2)
    print("Thank you for your cooperation. You may now participate in the Dating Game.")
    Hobbies()
    break
