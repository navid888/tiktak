game=[[1,1,1],
    [1,1,1],
    [1,0,0,]]
d = ('   0, 1, 2')   
print(d)
for a,d in enumerate(game) :
        print(a,d)
d = ('   0, 1, 2')
print(d)

#radif
def win(gaming) :
    for x in game :
      print(x)
      if x.count(x[0]) == len(x)  and x[0] != 0 :
    
     
        print("winner")
win(game)

#soton
for y in range(len(game)) :
    s=[]
    for x in game :
        
        s.append(x[y])
       
    if s.count(s[0]) == len(s)  and s[0] != 0 :
       
       print("winner")
       