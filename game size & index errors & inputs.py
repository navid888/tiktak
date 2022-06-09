import itertools
import numpy
'''
game=[[1,1,1],
      [0,0,0],
      [0,0,0]]

'''



#error
def game_board(game_map, player=0 ,r=0 , s=0 , just_display=True ) 
    try :
        print("   "+"  ".join(str[i]) for i in game_size)
        for r,s in enumerate(game_size) :
            print(r,s)
        return game_ map , True    
    except indexerror as e :
        print ("Error = your input is wrong " , e)
        return game_map , False
    except exception as e : 
        print("error:something is wrong " ,e)
        return game_map , False


game_size=input("please enter your tic_tac_toe size :  " )
game = [[0 for i in game_size] for i in game_size]
print(game)

#radif
def win(gaming) :
    for r in game :
      
      if r.count(r[0]) == len(r)  and r[0] != 0 :
        game_won=True
        print(r,"winner radif")
        
       
        
win(game)

#soton
for y in range(len(game)) :
    s=[]
    for x in game :
        
        s.append(x[y])
       
    if s.count(s[0]) == len(s)  and s[0] != 0 :
        game_won=True
        print(s,"winner soton")
        
#ghotr
diag=d=[] 
for ix in range(len(game)) : 
  
    
    d.append(game[ix][ix]) 
    
if d.count(d[0]) == len(d)  and d[0] != 0 :
    game_won=True
    print(d,'winner diag')  
    
#ghotr2    
diag2=d2=[]           
for idx,idy in enumerate(reversed(range(len(game)))) :
    
    d2.append(game[idy][idx])
if d2.count(d2[0]) == len(d2)  and d2[0] != 0 :
    #print (d2)
    print(d2,"winner diag2")
    



#player choice & cycle
player=[1,2]
game_won=False
game=[[0,0,0],
      [0,0,0],
      [0,0,0]]
      

choice_player=itertools.cycle(player)
while not game_won: 
    current_player=next(choice_player)
    print(f"current_player :{current_player}")
    
#row and column choosing
#def game_board(r)
    
    

