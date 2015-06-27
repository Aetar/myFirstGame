#This is my first program something more advance then hello world i guess
#hope you all will like it and help me improve it 
#features i want to have in this hope somebody will help me with it
/*In the selection menu I want the program to return to the selection menu after an invalid selection,
The game play surely don't look like a game wish i knew the way to clear the screen rather then new 
lines comming down the screen
there must be a way to pause or return to the main menu after the game play completes,the console just closed 
after the game play finished.to stop that i put the input() function in line 106 */


import random

#Welcome screen 
print ("""
    ****Welcome to the dice roller****
 ***Lets see How lucky you are today***
         A GAME BY INDRONIL
 """)
#Selection menu
sel=input(
    """
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
=======
Input 1 -->[to play]
=======
Input 2 -->[to read Instructions]
=======
Input 3-->[to know about us]
=======

And Click

ENTER

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
\n \n 
""")

#selection logic 
         
if sel=="1":
          print ("Lets Roll")
elif sel=="2":
          print ("Instructions")
elif sel=="3":
          print("Rainy Day Productions (c)\n~Indronil")
else :
    print("Invalid input")

          #game play

num =random.randint(1,6)
unum=int(input("Guess what the dice will show \n \n \n "))
if num==1:
    print("""
---------
|       |
|   *   |
|       |
---------
\n \n \n \n""")
elif num==2:
    print("""
---------
| *     |
|       |
|     * |
---------
\n \n \n \n""")
elif num==3:
     print("""
---------
| *     |
|   *   |
|     * |
---------
\n \n \n \n""")
elif num==4:
     print("""
---------
| *   * |
|       |
| *   * |
---------
\n \n \n \n""")
elif num==5:
    print("""
---------
| *   * |
|   *   |
| *   * |
---------
\n \n \n \n""")
elif num==6:
      print("""
---------
| * * * |
|       |
| * * * |
---------
\n \n \n \n""")
if num==unum:
    print (" You seem to be lucky \n \n \n \n ")
else :
    print (" sorry better luck next time  \n \n \n \n")
input()



