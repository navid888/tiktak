import itertools
game=[[0,0,0],
      [0,0,0],
      [0,0,0]]
d = ('   0, 1, 2')   
print(d)
for a,d in enumerate(game) :
        print(a,d)
d = ('   0, 1, 2')
print(d)

#radif
def win(gaming) :
    for x in game :
      
      if x.count(x[0]) == len(x)  and x[0] != 0 :
        print(x,"winner radif")
     
        
win(game)

#soton
for y in range(len(game)) :
    s=[]
    for x in game :
        
        s.append(x[y])
       
    if s.count(s[0]) == len(s)  and s[0] != 0 :
       #print(s)
       print(s,"winner soton")

#ghotr
diag=d=[] 
for ix in range(len(game)) : 
  
    
    d.append(game[ix][ix]) 
    
if d.count(d[0]) == len(d)  and d[0] != 0 :
   # print(d)
    print(d,'winner diag')  

#ghotr2    
diag2=d2=[]           
for idx,idy in enumerate(reversed(range(len(game)))) :
    
    d2.append(game[idy][idx])
if d2.count(d2[0]) == len(d2)  and d2[0] != 0 :
    #print (d2)
    print(d2,"winner diag2")

player=[1,2]
game_won=False
game=[[0,0,0],
      [0,0,0],
      [0,0,0]]
      

choice_player=itertools.cycle(player)
while not game_won: 
    current_player=next(choice_player)
    print(f"current_player :{current_player}")

