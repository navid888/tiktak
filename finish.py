import itertools
#------------------------------------------------------------------------
#------------------------------------------------------------------------
def win(game):

 	def all_same(L):
 		if l.count(l[0]) == len(l) and l[0] != 0 :
 			return True
        else:
 	    	return False
#------------------------------------------------------------------------
 	#radif

for x in game :
	    print(x)
	    if all_same(x) 

	    		print(F" player {x[0]} is the winner horizantally ! ")

	    		return True
#------------------------------------------------------------------------
	#soton=column

	
	for y in range(len(game)) :
		s=[]

		for x in game:
				s.append(x[y])
		if all_same(s) :

	    		print(F" player {s[0]} is the winner soton ! ")

	    		return True

		#if s.count(s[0]) == len(s) and s[0] != 0 :
			#print( s[0] , " winner soton")
#------------------------------------------------------------------------
	#ghotr1=diagonally1

	    d1 =[]

	    for ix in range(len(game)) :
	    		d1.append(game[ix][ix])
	    if all_same(d1) :

	    		print(F" player {d1[0]} is the winner diagonally ! ")

	    		return True
	    #if  d1.count(d1[0]) == len(d1) and d1[0] != 0 :
	    	#print( d1 , "winner diagonally 1")
#------------------------------------------------------------------------
	#ghotr2=diagonally2

		d2=[]

		for y,x in enumerate(reversed(range(len(game)))) :
		 		d2.append(game[x][y])

		if all_same(d2) :

	    		print(F" player {d2[0]} is the winner diagonally ! ")

	    		return True
		#if d2.count(d2[0]) == len(d2) and d2[0] != 0 :
		 	#print(d[0] , "winner diagonally")

#------------------------------------------------------------------------
#------------------------------------------------------------------------
#error
def game_board(game_map, player=0 ,r=0 , s=0 , just_display=True) :
    try :
        print("   "+"  ".join([str(i) for i in range(len(game_map))]))
        if not just_display :
            game_map[r][s] = player    
        for r,s in enumerate(game_size) :
            print(r,s)
        return game_map , True    
    except indexerror as e :
        print ("Error = your input is wrong " , e)
        return game_map , False
    except exception as e : 
        print("error:something is wrong " ,e)
        return game_map , False
#------------------------------------------------------------------------
#------------------------------------------------------------------------


#player choice & cycle
play = True
player=[1,2]
while play :
    game_size=int(input("please enter your tic_tac_toe size :  " ))
    game = [[0 for i in range(game_size)] for i in range(game_size)]
    game_won = False
    game , _ = game_board(game , just_display = True)
    choice_player=itertools.cycle(player)

    while not game_won: 
        current_player=next(choice_player)
        print(f"current_player :{current_player}")
        played = False

        while not played :
        s_choise = int(input("choose column from (0 , 1 , 2 , ....): "))
        r_choise = int(input("choose row from (0 , 1 , 2 , ....): "))
        game , played = game_board(game , current_player , s_choise , r_choise)

    if win(game) : 
        game_won = True
        again = input("do you want to play agian ? ( y / n ) ")
        if again.lower() == "y" :
            print("restaring..... let's play again ")
        elif again.lower() == "n" :

            print("byeeeeee") 
            play = False
        else :
            print(" not a valid answer , so see u later again ")
            play = False




    
    

