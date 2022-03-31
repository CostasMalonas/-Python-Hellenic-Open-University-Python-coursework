# Multiline string με τις πληροφορίες των υπαλλήλων
employees = """Γιώργος Γεωργίου,m,eng,project1 project3 
 Μαρία Ρήγα,f,eng,project2 
 Κατερίνα Σελή,f,secr,project1 project2 
 Νίκος Πάλης,m,tech,project2 
 Λίνα Πενταγιά,f,eng,project1 
 Ρένα Ντορ,f,secr,project3 project2 
 Τζον Κλης,m,tech,project1 project2 
 Λάκης Λαζός,m,eng,project2 
 Μαρίνα Μαρή,f,eng,project3 
 Ζήσης Χελάς,m,tech,project1 project2"""

# αρχικοποίηση των συνόλων


def load_sets(employees):
    # φόρτωμα των στοιχείων του πίνακα εργαζομένων στα σύνολα
    employees_ls = employees.splitlines() # Χωρίζουμε το multiline string σε γραμμές και το εκχωρούμε σε λίστα
    # Δημιουργία κενών sets
    m = set()
    f = set()
    eng = set()
    tech = set()
    secr = set()
    p1 = set() 
    p2 = set() 
    p3 = set() 
    
    dict_set = {} # Δημιουργία λεξικού που θα έχει σαν key το όνομα του set και σαν value το set
    
    # Παίρνουμε κάθε line από το employees_list και ελέγχουμε τι γράμματα υπάρχουν
    # μέσα σε κάθε string. Κάθε φορά κάνουμε split το string μας στο 1ο κόμμα
    # και παίρνουμε το όνομα των υπαλλήλων
    for line in employees_ls:
        if 'm' in line:
            m.add(line.split(',')[0]) # Χώρισε στο 1ο κόμμα
        if 'f' in line:
            f.add(line.split(',')[0]) # Χώρισε στο 1ο κόμμα
            
        if 'eng' in line:
            eng.add(line.split(',')[0])
    
        if 'tech' in line:
            tech.add(line.split(',')[0])
    
        if 'secr' in line:
            secr.add(line.split(',')[0])
        
        if 'project1' in line:
            p1.add(line.split(',')[0]) 

        if 'project2' in line:
            p2.add(line.split(',')[0]) 

        if 'project3' in line:
            p3.add(line.split(',')[0])                


    


    keys_list = ['m', 'f', 'eng', 'tech', 'secr', 'p1', 'p2', 'p3']
    set_list = [m, f, eng, tech, secr, p1, p2, p3]

    # Δημιουργία του λεξικού
    set_dict = {}
    for i, key in enumerate(keys_list): # Η enumerate επιστρέφει έναν αριθμό από 0 έως len(key_list) - 1 και τον εκχωρεί στο i  
        set_dict[key] = set_list[i]
        
    return set_dict


# εκτύπωση set
def show_set(hint, s):
    print(hint + ':', s) # Τυπώνουμε το hint string μαζί με το set


    

# ΑΠΑΝΤΗΣΕΙΣ ΣΤΑ ΕΡΩΤΗΜΑΤΑ
# οι άνδρες που δουλεύουν στο project1
def men_project1(set_m, set_p1):
    p1_m_set = set() 
    for val in set_m: # Αν ένα όνομα υπάρχει στο set_m (males)
        if val in set_p1: # και υπάρχει και στο set_p1 (project_1)
            p1_m_set.add(val) # εκχώρησε το στο set p1_m_set
        
    print('ΑΝΔΡΕΣ ΠΟΥ ΔΟΥΛΕΥΟΥΝ ΣΤΟ P1: ', p1_m_set)


# όλοι όσοι δουλεύουν στο project1 αλλά όχι στο project2 ή project3
def project1_not_project2_not_project3(set_p1, set_p2, set_p3):
    
    # Από το set_p1 αφαίρεσε τα values που υπάρχουν στο set_p2 και από το set
    # που προκύπτει αφαίρεσε τα values που υπάρχουν στο set_p3
    print('ΔΟΥΛΕΥΟΥΝ ΜΟΝΟ ΣΤΟ P1:' , ((set_p1 - set_p2) - set_p3))

# οι γυναίκες μηχανικοί
def f_eng(set_f, set_eng):
    # Η τομή (μέθοδος intersection) του set με τις γυναίκες και του set με τους μηχανικούς 
    print('ΓΥΝΑΙΚΕΣ ΜΗΧΑΝΙΚΟΙ: ', set_f.intersection(set_eng))


# όλοι οι τεχνικοί που δουλεύουν είτε στο project1 ή στο project2
def tech_p1_p2(set_tech, set_p1, set_p2):
    # Η τομή (μέθοδος intersection) του set των τεχνικών με το Set αυτών που δουλεύουν στο project 1
    # και η ένωση αυτού του συνόλου με την τομή των τεχνικών που δουλεύουν στο project 2
    print('ΤΕΧΝΙΚΟΙ ΠΟΥ ΔΟΥΛΕΥΟΥΝ ΣΤΟ P1 Η ΣΤΟ P2: ', set_tech.intersection(set_p1).union(set_tech.intersection(set_p2)))
    


# οι άνδρες μηχανικοί που δεν δουλεύουν στο project2
def m_eng_not_p2(set_m, set_eng, set_p2):
    # Η τομή του σετ των ανδρών με το σετ των μηχανικών - το set αυτών που δουλεύουν στο project 2
    print('ΑΝΔΡΕΣ ΜΗΧΑΝΙΚΟΙ ΠΟΥ ΔΕΝ ΔΟΥΛΕΥΟΥΝ ΣΤΟ P2: ', set_m.intersection(set_eng) - set_p2)


#### κυρίως πρόγραμμα ####
# αρχικά σύνολα



set_dict = {}
set_dict = load_sets(employees)

for key, value in set_dict.items():
    show_set(key, value)
    
    
### κλήση συναρτήσεων
print("ΑΠΑΝΤΗΣΕΙΣ ΣΤΑ ΕΡΩΤΗΜΑΤΑ:")
men_project1(set_dict['m'], set_dict['p1'])

project1_not_project2_not_project3(set_dict['p1'], set_dict['p2'], set_dict['p3'])
f_eng(set_dict['f'], set_dict['eng'])
tech_p1_p2(set_dict['tech'], set_dict['p1'], set_dict['p2'])
m_eng_not_p2(set_dict['m'], set_dict['eng'], set_dict['p2'])
