v=input().split('\n')            #list_of_inputs
n = int(v[0])                    # number of customer
l=len(v)                         # number_of_inputs


""" INITIATION"""
#   s=[]                         Note: I dont think s is needed here
like_person =[]                  # NESTED LIST which store all the like-ingredients of each person
dis_person = []                  # NESTED LIST which store all the like-ingredients of each person              
dislike={}                       # DICTIONARY which store all ingredients and their like score
like={}                          # DICTIONARY which store all ingredients and their dislike score
ingredients=[]                   # LIST of all ingredients



"""APPEND LIST and DICT"""
for i in range(1,l,2):
    a=v[i].split()[1:]           # Take the ith and i+1th element of list_of_input V 
    b=v[i+1].split()[1:]         # Excluded the first element (number of ingredients in each list)
    like_person.append(a)        
    dis_person.append(b)
    for u in a:                  # I think this is more efficient if we get rid of s
        if u not in like:        # And append all item in this for loop
            like[u] = 1
        
        else:
            like[u] += 1
        if u not in ingredients:
            ingredients.append(u)
    for u in b:
        if u not in dislike:
            dislike[u] = 1
        
        else:
            dislike[u] += 1
        if u not in ingredients:
            ingredients.append(u)
    
        

"""for i in s:                 #this is the code of Shubh but I simplify it by the upper part
    
    
    
    
    
    for j in i[1:]:
        if j not in ingredients:
            ingredients.append(j)
for i in range(len(s)):
    for j in s[i][1:]:
        if i%2==0: 
            continue
        else:
            if j not in dislike:
                dislike[j]=1
            else:
                dislike[j]+=1
for i in dislike:
    for j in range(len(s)):
        if j%2==0:
            if i in s[j]:
                if i not in like:
                    like[i]=1
                else:
                    like[i]+=1"""
                    
                    
                    
  
"""SECOND INITIATION"""
add=[i for i in ingredients if i not in dislike] # List of no-dislike ingredients
z= []                          # LIST OF ELEMENT WHERE LIKE = DISLIKE
worth = 0                      # Score to determine if it is worth it to include the ingredients



"""ADD INGREDIENTS"""
for i in like:
    if i in dislike:
        if like[i]>dislike[i]:
            add.append(i)
        elif like[i] == dislike[i]:                       # CHECK FOR A BETTER SOLUTION
            z.append(i)
        #else:                                   IGNORE THIS
        #   z.append(i)

for i in z:                                   # For each element in Z which have like <= dislike
   for p in range(len(like_person)):          # Loop through the nested list i mention above                                                 
        if i in dis_person[p]:                  
            if all([i in add for i in like_person[p]]):
                continue
            else:
                if i not in add:
                    add.append(i)
        #            worth += 1
               
        #if like[i]+worth>dislike[i]:      
                
        #    add.append(i)
        #    worth = 0
                
                    
                    
                
       
            
            
            
 
        continue


add.insert(0, len(add))
print(*add)

  



