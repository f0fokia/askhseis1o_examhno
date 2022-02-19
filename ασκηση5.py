f = open("trialcode.txt", "r")  # ανοιγω το κειμενο
my_file = f.read().lower()  # αποθηκευω τα δεδομενα στο my_file ενω με την συναρτηση .lower() κανω ολο το κειμενο σε
# πεζα γραμματα
my_words = my_file.split(" ")  # διαχωριζω τις λεξεις μου σε μια λιστα αναλογα με το ποτε εχω κενο
mixed_words = []  # λιστα για τις λεξεις που διορθωνω
my_numbers = []  # αριθμοι των λεξεων που χρειαζονται διαγραφη


def fix_words(my_words):  # συναρτηση διορθωσης λεξεων
    count = -1  # μεταβλητη μετρησης του index του αντικειμενου
    for i in my_words:  # για καθε λεξη
        count = count + 1  # αθξηση μετρητη
        if not i.isalnum():  # αν η λεξη δεν ειναι αλφαριθμητική
            mixed_words.append(i.replace('.', '').replace(')', '').replace('(', '').replace(',',
                                                                                            ''))  # προσθεσε στην
            # λιστα mixed_words την λεξη χωρις
            # τους χαρακτηρες ) ( , .
            my_numbers.append(count)  # προσθεσε το index της λεξης στην λιστα my_numbers

    my_numbers.sort(reverse=True)  # βαλε τα στοιχεια σε φθινουσα σειρα

    for i in my_numbers:  # για καθε index
        my_words.pop(i)  # διεγραψε την λεξη που αντιστοιχει σε αυτο το index

    my_words += mixed_words  # προσθεσε τις διορθωμενες λεξεις


def most_popular_words(my_words):  # συναρτηση υπολογισμου μεγιστου αριθμου λεξεων σε λιστα
    max = 0  # αριθμος μεγιστων επαναληψεων της λεξης
    for i in my_words:  # για καθε λεξη στην λιστα
        if my_words.count(
                i) > max:  # αν ο αριμος που εχουμε την λεξη στην λσιτα ειναι μεγαλυτερος απο τον ηδη μεγαλυτερο
            max = my_words.count(i)  # κανε το max ισο με τον αριθμο αυτο
            top_word = i  # αποθηκευσε την λεξη αυτη στο top_word

    print("<<" + top_word + ">> and we find it " + str(
        max) + " times!")  # τυπωσε την λεξη και ποσες φορες εθεαθη
    for i in range(0, max):  # για οσες φορες εχουμε την λεξη
        my_words.remove(top_word)  # διεγραψε την λεξη αυτη


fix_words(my_words)  # καλουμε την συναρτηση ωστε να διορθωσουμε τις λεξεις
my_words2 = my_words[:]  # αντιγραφη της διορθωμενης λιστας
my_words3 = my_words[:]  # >> >> >>
print("Top 10 words and it's appearance:")
for i in range(1, 11):
    print(i, end=")")
    most_popular_words(my_words)

print("================================")
print("Top 3 starting 2 letters:")

my_list = []  # λιστα για την αλλαγη των λεξεων μας
for i in my_words2:  # για καθε λεξη
    my_list.append(i[:2])  # κρατα μονο τους 2 πρωτους χαρακτηρες
for i in range(0, 3):  # 3 φορες
    print(i, end=")")
    most_popular_words(my_list)  # καλουμε την συναρτηση

print("================================")
print("Top 3 starting 3 letters:")
my_list2 = []  # λιστα για την αλλαγη των λεξεων μας
for i in my_words3:  # για καθε λεξη
    my_list2.append(i[:3])  # κρατα μονο τους 3 πρωτους χαρακτηρες
for i in range(0, 3):  # 3 φορες
    print(i, end=")")
    most_popular_words(my_list2)  # καλουμε την συναρτηση