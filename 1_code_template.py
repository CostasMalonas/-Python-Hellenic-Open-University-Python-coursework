
### κυρίως πρόγραμμα ###


import random 

def generate_random_floats(n, m, seed=None):
    if seed: # Αν το seed δεν είναι ίσο με None,
        random.seed(seed) # καλούμε την μέθοδο seed της βιβλιοθήκης random και ορίζουμε το seed
    
    ls = [] # Κενή λίστα
    for num in range(n): # Για n φορές, 
        ls.append(random.uniform(-m, m)) # θα δημιουργηθούν τυχαίοι αριθμοί στο διάστημα -m, m και θα γίνουν append στην λίστα
    
    return ls # Τέλος επιστρέφουμε την λίστα





def find_max_gap(ls):
    # Συνάρτηση για να βρούμε την μέγιστη διαφορά μεταξύ στοιχείων της λίστας
    ls.sort() # Ταξινομούμε την λίστα μας σε αύξουσα σειρά
    
    vmin = ls[0] # Ορίζουμε σαν min το πρώτο στοιχείο της λίστας
    dmax = 0 # Αρχικοποιούμε το dmax με 0
    
    # Για len(ls) φορές αν η διαφορά του στοιχείου που βρίσκεται στο ls[i] με το vmin είναι μεγαλύτερη
    # από το dmax, εκχωρούμε στο dmax αυτή την διαφορά. Τέλος επιστρέφουμε το dmax
    for i in range(len(ls)):
        if(ls[i] - vmin > dmax):
            dmax = ls[i] - vmin
    return dmax



def present_list(ls):
    # Συνάρτηση για να τυπώσουμε την λίστα
    str_ls = [] # Κενή λίστα
    
    for el in ls: # Για κάθε element στην λίστα ls,
        str_ls.append(str(el)) # το μετατρέπουμε από αριθμο σε str και το κάνουμε append στην str_ls.
        
    print('Η τυχαια λίστα είναι ', ','.join(str_ls)) # Τυπώνουμε την λίστα str_ls ενώ κάνουμε join τα στοιχεία της με ','
    




# ζήτησε από τον χρήστη το πλήθος των τυχαίων αριθμών
n = int(input('Δώσε πλήθος τυχαίων αριθμών: '))

# ζήτησε από τον χρήστη το διάστημα -m, m
m = int(input('Δώσε διάστημα -m, m: ')) 

# ζήτησε από τον χρήστη την τιμή του σπόρου seed
seed = input('Δώσε seed: ')
if seed == '':
    seed = None 
else:
    seed = int(seed)


# δημιουργία λίστας τυχαίων αριθμών
ls = generate_random_floats(n, m, seed)
print(ls)



# παρουσίαση της λίστας
present_list(ls)

# υπολογισμός μέγιστης απόστασης
print('Η μέγιστη απόσταση είναι: ', find_max_gap(ls))





