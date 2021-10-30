
def isAnagram(s, t):
    hmap = {}

    if len(s) != len(t):
        return False
    
    for letter in s: 
        if not letter in hmap:
            hmap[letter] = 1
        else:
            hmap[letter] += 1
    
        
    for letter in t:
        if not letter in hmap:
            return False
        else:
            hmap[letter] -= 1
            if hmap[letter] == 0:
                del hmap[letter]
    
            
    return True
    
a="race"
b="rare"
print(isAnagram(a,b))                 
    

