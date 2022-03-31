from math import sin, cos, sqrt, atan2, radians


# Ορίζουμε την multiline συμβολοσιρά μας με τα στοιχεία των αεροδρομίων
airport_data = """
Alexandroupoli	40.855869°N 25.956264°E
Athens 37.936389°N 23.947222°E
Chania	35.531667°N 24.149722°E
Chios	38.343056°N 26.140556°E
Corfu 39.601944°N 19.911667°E
Heraklion	35.339722°N 25.180278°E
Kalamata	37.068333°N 22.025556°E
Kavala 40.913333°N 24.619167°E
Kefalonia	38.12°N 20.500278°E
Kos	36.793336°N 27.091667°E
Lemnos	39.917072°N 25.236308°E
Mytilene	39.0567°N 26.5994°E
Paros	37.020833°N 25.113056°E
Rhodes	36.405419°N 28.086192°E
Samos	37.6891°N 26.9116°E
Thessaloniki 40.519722°N 22.970833°E
Zakynthos 37.750833°N 20.884167°E"""

# Σε αυτή την λίστα θα εκχωρήσουμε tuples που θα είναι της μορφής,
# (Όνομα αεροδρομίου, αριθμός°N, αριθμός°E)
airports = []


def process_airports(airport_data):
    # συνάρτηση που διαβάζει τα στοιχεία αεροδρομίων και γεμίζει τη λίστα airports
    
    airport_data_list = airport_data.split() # Χωρίζουμε το string μας στα κενά με την split() μέθοδο
    airports = [] # Κενή λίστα airports
    

    for idx in range(0, len(airport_data_list), 3): # Για idx από 0 μέχρι len(airport_data_list) με βήμα 3
        air_name = airport_data_list[idx] # Παίρνουμε από την λίστα το όνομα του αεροδρομίου
        
        # Παίρνουμε το °N number και αφαορούμε το °N με την μέθοδο replace
        # Έπειτα μετατρέπουμε αυτόν τον αριθμό σε float και τον εκχωρούμε στο elem1
        elem1 = float(airport_data_list[idx + 1].replace('°N', ''))  
        
        # Η ίδια διαδικασία για το elem2
        elem2 = float(airport_data_list[idx + 2].replace('°E', ''))
        
        # Κάνουμε append το tuple με τα παραπάνω στοιχεία στην λίστα airports
        airports.append((air_name, elem1, elem2))
        
        
    return airports # Επιστρέφουμε την λίστα με τα tuples


def distance(lat1, lon1, lat2, lon2):
    # υπολογισμός της απόστασης μεταξύ των γεωγραφικών συντεταγμένων lon1, lat1 και
    # των γεωγραφικών συντεταγμένων lon2, lat2 χρησιμοποιώντας τον τύπο Haversine
    # https://en.wikipedia.org/wiki/Haversine_formula

    R = 6373.0  # ακτίνα της γης σε km
    lat1, lon1 = radians(lat1), radians(lon1) 
    lat2, lon2 = radians(lat2), radians(lon2)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    d = R * c
    return d


def menu():
    # συνάρτηση που παρουσιάζει το μενού επιλογών και χειρίζεται τις
    # απαντήσεις του χρήστη
    
    # Multiline string με την υπόδειξη προς τον χρήστη που θα τυπώνεται σε κάθε loop
    ypodeiksh = """
        1 Alexandroupoli\
        2 Athens \
        3 Chania \
        4 Chios \
        5 Corfu \
        6 Heraklion \
        7 Kalamata \
        8 Kavala \
        9 Kefalonia \
        10 Kos \
        11 Lemnos \
        12 Mytilene \
        13 Paros \
        14 Rhodes \
        15 Samos \
        16 Thessaloniki \
        17 Zakynthos\n"""
        
    while True: # Ατέρμων βρόχος
        print('Επιλέξτε δύο αεροδρόμια i, j για τον υπολογισμό της απόστασης τους ή min για ελάχιστη απόσταση') # Μήνυμα προς τον χρήστη
        print(ypodeiksh) # Τυπώουμε την παραπάνω υπόδειξη
          
        # Παίρνουμε το string που επιστρέφεται από το input() και 
        # το κάνουμε split() στα κόμματα.
        choice = input('Δώσε επιλογή: ').split(',') 
        
        if choice[0] == '': # Αν το 1ο στοιχείο της λίστας choice είναι το empty string επιστρέφουμε μια λίστα με
        # έναν κενό χαρακτήρα.
            print('Πάτησες "enter"')
            return choice
            
        # Αν το πλήθος των στοιχείων της choice είναι 1 αλλά το 1ο στοιχείο δεν είναι min
        # η επιλογή του χρήστη δεν είναι έγκυρη, τυπώνεται μήνυμα και κάνουμε continue 
        # από την αρχή του while loop
        elif len(choice) == 1 and choice[0] != 'min':
            print('Δώσε έγκυρη επιλογή\n')
            continue
        
        # Αν το len(choice) == 1 και το choice[0] == 'min'
        # τότε επιστρέφουμε την λίστα ['min']
        elif len(choice) == 1 and choice[0] == 'min':
            print('Επέλεξες "min"')
            return choice
        
        # Αν το len(choice) == 2 και το 1ο και 2ο στοιχείο είναι ψηφία (το ελέγχουμε με την μέθοδο isdigit()),
        # μπαίνουμε μέσα στο elif..
        elif len(choice) == 2 and (choice[0].isdigit() and choice[1].isdigit()):
            # Αν το 1ο και 2ο στοιχείο είναι στο range [1, 17], επιστρέφουμε ένα
            # tuple με το 1ο και 2ο στοιχείο σαν ακέραιους. Αλλιώς τυπώνουμε μήνυμα να δοθεί 
            # έγκυρη επιλογή
            if int(choice[0]) in range(1, 18) and int(choice[1]) in range(1, 18):
                 print('Επέστρεψε την πλειάδα των αεροδρομίων')
                 return (int(choice[0]), int(choice[1]))
            else:
                print('Δώσε έγκυρη επιλογή\n')
                continue 
        
        # Αν len(choice) == 2 και το 1ο και 2ο στοιχείο δεν είναι αριθμοί ξαναδίνουμε είσοδο
        elif len(choice) == 2 and not choice[0].isdigit() and not choice[1].isdigit():
            print('Δώσε έγκυρη επιλογή\n')
            continue
        else:
            # Αν δώσουμε παραπάνω από 2 τιμές τυπώνεται το παρακάτω μήνυμα
            print('Έδωσες πολλές τιμές\n')
            continue
                
            
                    


def min_distance(airport_list):
    # συνάρτηση που υπολογίζει την ελάχιστη μεταξύ των αεροδρομίων της λίστας airports
    
    
    airports_names_dict = {} # Λεξικό που θα αποθηκεύσουμε σαν key έναν αριθμό από το 1 εως το 17 και σαν value το όνομα του αεροδρομίου
    for key in range(1, 18):
        airports_names_dict[key] = airport_list[key-1][0]
        
    #print(airports_names_dict)
    
    dist_list = [] # Λίστα που θα αποθηκεύσουμε τις λίστες που περιέχουν την απόσταση κάθε αεροδρομίου από κάθε άλλο
    
    # Για len(airport_list) φορές εκχωρούμε στην λίστα dist_list, λίστες με την απόσταση κάθε,
    # αεροδρομίου προς κάθε άλλο
    for num in range(len(airport_list)):
        temp = []
        for num2 in range(len(airport_list)):
            temp.append(distance(airport_list[num][1], airport_list[num][2], airport_list[num2][1], airport_list[num2][2]))
        dist_list.append(temp)
    
    # Λεξικό με τον αριθμό κάθε αεροδρομίου σαν key και σαν value την λίστα με τις αποστάσεις
    # του αεροδρομίου προς κάθε άλλο (συμπεριλαμβανομένου προς τον εαυτό του)    
    airports_dict = {} 
    for key in range(len(dist_list)):
        airports_dict[key + 1] = dist_list[key]
        
    # Αφαιρούμε το 0.0 (απόσταση αεροδρομίου από τον εαυτό του) από κάθε λίστα αποστάσεων του λεξικού     
    for key in airports_dict:
        airports_dict[key].remove(0.0) 
        
    min_airports_dict = {} # Λεξικό με αριθμό κάθε αεροδρομίου σαν key και min distance σαν value
    
    # Δημιουργούμε ένα λεξικό με την ελάχιστη απόσταση του αεροδρομίου (key) και κάποιου άλλου αεροδρομίου
    for key in airports_dict:
        min_airports_dict[key] = min(airports_dict[key])
        
        
    # Παίρνουμε το πρώτο key με το minimum value από όλο το λεξικό
    # source: https://stackoverflow.com/questions/3282823/get-the-key-corresponding-to-the-minimum-value-within-a-dictionary
    min_key_first  = min(min_airports_dict, key=min_airports_dict.get)
    
    # Βρίσκουμε πιο άλλο key έχει value ίσο με το minimum value του key που βρήμαμε παραπάνω
    for key in range(min_key_first + 1, 18):
        if min_airports_dict[key] == min_airports_dict[min_key_first]:
            min_key_second = key
            
    # Τυπώνουμε την απόσταση με ακρίβεια ενός δεκαδικού ψηφίου
    print('Τα πλησιέστερα αεροδρόμια είναι ', airports_names_dict[min_key_first], 'και ', airports_names_dict[min_key_second] \
          , ' με απόσταση {0:.1f}'.format(min_airports_dict[min_key_first]))
    
    

            
    



### κυρίως πρόγραμμα ###

while True: # Ατέρμων βρόχος
   
    airport_list = process_airports(airport_data) # Δημιουργούμε την λίστα με τα αεροδρόμια
    
     
    choice = menu() # Καλούμε την menu() συνάρτηση για να δώσουμε την επιλογή μας
    
    # Ελέγχουμε τι επέστρεψε η menu()
    if choice[0] == '':
        print('Bye Bye')
        break
    elif len(choice) == 2:
        print('Η απόσταση είναι: {0:.2f}'.format(distance( airport_list[choice[0] - 1][1], airport_list[choice[0] - 1][2], 
                                             airport_list[choice[1] - 1][1], airport_list[choice[1] - 1][2] )))
        #print(airport_list[choice[0] - 1][1])
        #print('Hey')
    elif choice[0] == 'min':
        min_distance(airport_list)
        
    else:
        pass
        

## επαναληπτική κλήση μενού και διαχείριση απάντησης χρήστη














