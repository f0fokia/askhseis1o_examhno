f = open("trialcode.txt", "r")  # ανοιγω το αρχειο
my_file = f.read()  # αποθηκευω το εσωτερικο του στο my_file


def toBinary(my_words):  # συναρτηση μετατρωπης λεξεων σε δυαδικους αριθμους
    l, m = [], []
    final = ''
    for i in my_words:  # για καθε γραμμα
        l.append(ord(i))  # προσθετω στην L λιστα μου το unicode του γραμματος
    for i in l:  # για καθε unicode του L
        m.append(int(bin(i)[2:]))  # προσθετω στην Μ λιστα τον δυαδικο αριθμο απο το 3ο ψηφειο και μετα
    for i in m:  # για καθε δυαδικο αριθμο
        final = final + str(i)  # "κολλαω" στο τελλος τον επομενο δυαδικο

    return final


def count_zeros(result):  # συναρτηση μετρητη μηδενικων
    i = 0  # η μεταβλητη μου που με βοηθαει να μετρησω ολους τους χαρακτηρες
    count = 0  # μεταβλητη που μετραει ποσα 0 ειναι στην σειρα
    biggest = 0  # μεταβλητη που κραταει τον μεγιστο αριθμο απο 0
    z = len(result)  # μεταβλητη για τον αριθμο των συνολικων ψηφιων

    while i != z:  # οσο η μεταβλητη i δεν ειναι ιση με τον συνολικο αριθμο των ψηφιων
        if result[i] == '0':  # αν το συγκεκριμενη ψηφιο ειναι 0
            count = count + 1  # προσθεσε 1 στο count
        else:  # αλλιως
            if count > biggest:  # αν το count ειναι μεγαλυτερο απο το biggest
                biggest = count  # αλλαξε την τιμη του biggest σε count
            count = 0  # μηδενισμος count
        i = i + 1  # προσθετουμε 1 στο i για το επομενο ψηφειο
    print("Most 0 in a row are:" + str(biggest))  # αποτελεσματα


def count_ones(result):
    i = 0
    count = 0
    biggest = 0
    z = len(result)

    while i != z:
        if result[i] == '1':
            count = count + 1
        else:
            if count > biggest:
                biggest = count
            count = 0
        i = i + 1
    print("Most 1 in a row are:" + str(biggest))


result = toBinary(my_file)  # καλω την συναρτηση
print(result)
count_zeros(result)  # καλω την συναρτηση
count_ones(result)  # καλω την συναρτηση