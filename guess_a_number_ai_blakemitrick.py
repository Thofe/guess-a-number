## Number Genie
## Blake Mitrick
## 8/16/2016

def startscreen():
    print("▂▃▅▇█▓▒░۩۞۩    ヽ༼ຈل͜ຈ༽ﾉ   ۩۞۩░▒▓█▇▅▃▂")
    print("▂▃▅▇█▓▒░۩۞۩              ۩۞۩░▒▓█▇▅▃▂")
    print("▂▃▅▇█▓▒░۩۞۩ Number Genie ۩۞۩░▒▓█▇▅▃▂")
    print("▂▃▅▇█▓▒░۩۞۩              ۩۞۩░▒▓█▇▅▃▂")
    print("▂▃▅▇█▓▒░۩۞۩Press any key ۩۞۩░▒▓█▇▅▃▂")
    print("▂▃▅▇█▓▒░۩۞۩   to play    ۩۞۩░▒▓█▇▅▃▂")
    input()

def play():
    
    got_it= False

    print("I am the Number Genie.")
    print("Think of a number between 2 numbers of your choice and I will be able to guess it.")
    print("I will guess a number and If I get it correct say 'Yes' or 'Y'.")
    print("If I'm not correct you will tell me higher or lower.")
    print("Press any key when you are ready to play")
    input()
    low = int(input("Pick the low"))
    high= int(input("Pick the high"))



    while got_it== False:
        guess = (high+low) // 2
        answer= input("Is your number " + str(guess)+ "?")

        if answer.lower() == "higher" or answer.lower() == "h":
            low = guess + 1
        elif answer.lower() == "lower" or answer.lower() == "l":
            high = guess + 1
        elif answer.lower() == "yes" or answer.lower() == "y":
            print("I told tou I could guess your number")
            got_it= True
        else:
            print("I don't quite understand your answer, please tell me again.")
       

    
def play_again():
    while True:
        answer = input("Would you like to play again?")
        
        if answer.lower() == 'no' or answer.lower() == 'n':
            return False
        elif answer.lower() == 'yes' or answer.lower() == 'y':
            return True

        print("What are u dum?!?!?!?!?!? " + answer +" is neither yes nor no")

startscreen()
again = True

while again == True:
    play()
    again = play_again()

print("""
          _____                    _____                    _____                    _____          
         /\    \                  /\    \                  /\    \                  /\    \         
        /::\    \                /::\    \                /::\____\                /::\    \        
       /::::\    \              /::::\    \              /::::|   |               /::::\    \       
      /::::::\    \            /::::::\    \            /:::::|   |              /::::::\    \      
     /:::/\:::\    \          /:::/\:::\    \          /::::::|   |             /:::/\:::\    \     
    /:::/  \:::\    \        /:::/__\:::\    \        /:::/|::|   |            /:::/__\:::\    \    
   /:::/    \:::\    \      /::::\   \:::\    \      /:::/ |::|   |           /::::\   \:::\    \   
  /:::/    / \:::\    \    /::::::\   \:::\    \    /:::/  |::|___|______    /::::::\   \:::\    \  
 /:::/    /   \:::\ ___\  /:::/\:::\   \:::\    \  /:::/   |::::::::\    \  /:::/\:::\   \:::\    \ 
/:::/____/  ___\:::|    |/:::/  \:::\   \:::\____\/:::/    |:::::::::\____\/:::/__\:::\   \:::\____\

\:::\    \ /\  /:::|____|\::/    \:::\  /:::/    /\::/    / ~~~~~/:::/    /\:::\   \:::\   \::/    /
 \:::\    /::\ \::/    /  \/____/ \:::\/:::/    /  \/____/      /:::/    /  \:::\   \:::\   \/____/ 
  \:::\   \:::\ \/____/            \::::::/    /               /:::/    /    \:::\   \:::\    \     
   \:::\   \:::\____\               \::::/    /               /:::/    /      \:::\   \:::\____\    
    \:::\  /:::/    /               /:::/    /               /:::/    /        \:::\   \::/    /    
     \:::\/:::/    /               /:::/    /               /:::/    /          \:::\   \/____/     
      \::::::/    /               /:::/    /               /:::/    /            \:::\    \         
       \::::/    /               /:::/    /               /:::/    /              \:::\____\        
        \::/____/                \::/    /                \::/    /                \::/    /        
                                  \/____/                  \/____/                  \/____/         
                                                                                                    
""")                                                                                                                                                                                                        
print("""
         _______                   _____                    _____                    _____          
        /::\    \                 /\    \                  /\    \                  /\    \         
       /::::\    \               /::\____\                /::\    \                /::\    \        
      /::::::\    \             /:::/    /               /::::\    \              /::::\    \       
     /::::::::\    \           /:::/    /               /::::::\    \            /::::::\    \      
    /:::/~~\:::\    \         /:::/    /               /:::/\:::\    \          /:::/\:::\    \     
   /:::/    \:::\    \       /:::/____/               /:::/__\:::\    \        /:::/__\:::\    \    
  /:::/    / \:::\    \      |::|    |               /::::\   \:::\    \      /::::\   \:::\    \   
 /:::/____/   \:::\____\     |::|    |     _____    /::::::\   \:::\    \    /::::::\   \:::\    \  
|:::|    |     |:::|    |    |::|    |    /\    \  /:::/\:::\   \:::\    \  /:::/\:::\   \:::\____\ 
|:::|____|     |:::|    |    |::|    |   /::\____\/:::/__\:::\   \:::\____\/:::/  \:::\   \:::|    |
 \:::\    \   /:::/    /     |::|    |  /:::/    /\:::\   \:::\   \::/    /\::/   |::::\  /:::|____|
  \:::\    \ /:::/    /      |::|    | /:::/    /  \:::\   \:::\   \/____/  \/____|:::::\/:::/    / 
   \:::\    /:::/    /       |::|____|/:::/    /    \:::\   \:::\    \            |:::::::::/    /  
    \:::\__/:::/    /        |:::::::::::/    /      \:::\   \:::\____\           |::|\::::/    /   
     \::::::::/    /         \::::::::::/____/        \:::\   \::/    /           |::| \::/____/    
      \::::::/    /           ~~~~~~~~~~               \:::\   \/____/            |::|  ~|          
       \::::/    /                                      \:::\    \                |::|   |          
        \::/____/                                        \:::\____\               \::|   |          
         ~~                                               \::/    /                \:|   |          
                                                           \/____/                  \|___|          
                                                                                                      
""")

while True:
    print("▂▃▅▇█▓▒░۩۞۩ Game made by Blake Mitrick on 9/8/2016  ۩۞۩░▒▓█▇▅▃▂")
    print("▂▃▅▇█▓▒░۩۞۩          You are now stuck here         ۩۞۩░▒▓█▇▅▃▂")
