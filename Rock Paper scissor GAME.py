import random

def lo():
    if (player =="S")or (player =="P")or (player =="R"):
        
        if (player == "R" or player == "p" or player == 'S'):
            if ((player =='R'and cpu == "S")or(player =='P'and cpu == "R")or(player =='S'and cpu == 'P')):
                print ('CPU: '+ cpu)
                print ('Player: '+ player)
                print("\n YOU WON !\n\n.")
                main()
        
        elif (player == cpu):
            print(f"CPU: {cpu}\nPlayer: {player}\n\n IT'S DRAW.\n\n")
            main()
        
        else:    
            print(f"Cpu: {cpu}\nPlayer: {player}\n\n YOU LOSE.\n\n")
            main()
    else:
      main()


def main():
    
    print ('   Rock , Paper , Scissors')
    print('--------------------------\n')
    global player,cpu
    print('Enter your choice \n1- for Rock press R \n2- for Paper press P\n3- for Scissor press S')
    player = input('ENTER YOUR CHOICE:  ')
    player = player.upper()

    print ('\n\n\n')

    cpu = str (random.randint(1,3))

    if (cpu == '1'):
        cpu = 'R'
        lo()
    elif (cpu == '2'):
        cpu = 'P'
        lo()
    elif (cpu == '3'):
        cpu = 'S'
        lo()
    #lo()    
    
       
main()