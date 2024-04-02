Τεχνολογίες Γραφημάτων και Εφαρμογές
===========

Σκοπός της εργασίας αυτής είναι η εξοικείωση σας με αλγορίθμους υπολογισμού node embeddings
σε γραφήματα. Ως παράδειγμα θα χρησιμοποιήσουμε ένα πολύ απλό αλγόριθμο που περιγράφεται
από τους Ahmed et al. [here](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/40839.pdf) .

Ο αλγόριθμος υπολογίζει για κάθε κόμβο ένα διάνυσμα Zi μέσω των οποίων μπορεί κανείς να
αποφασίσει την ύπαρξη μίας ακμής (i, j). Στην πιο απλή μορφή του μπορεί κανείς να χρησιμοποιήσει
ένα απλό μοντέλο εσωτερικού γινομένου όπου η πληροφορία της ύπαρξης μίας ακμής (i, j) μπορεί να
περιγραφεί αποτελεσματικά με το εσωτερικό γινόμενο ⟨Zi,Zj⟩.

# Πρώτο Μέρος


## 1. Σειριακή έκδοση του αλγορίθμου: `Sequential stochastic gradient descent`

Η υλοποιήση του αλγορίθμου βρίσκεται στο αρχείο `serial_algorithm.py` 

#### Run the serial_algorithm.py
```bash
python3 serial_algorithm.py
```


## 2. Αλγόριθμος με την βοήθεια της NetworkX

Η υλοποιήση του αλγορίθμου βρίσκεται στο αρχείο `algorithm_networkx.py`

#### Run the serial_algorithm.py
```bash
python3 algorithm_networkx.py
```

## 3. Εφαρμογή αλγορίθμου με δικά μας παραδείγματα

 Στο αρχείο `custom_examples.py` βρίσκεται η υλοποιήση των custom παραδειγμάτων για τον έλεγχο του αλγορίθμνου που υλοποιήσαμε. Με την εκτέλεση του αρχείου αρχικά θα εμφανιστούν τα αποτελέσματα από τα 2 πρώτα παραδείγματα (και extra μια απεικόνισή των γράφων). Όταν κλείσετε το παράθυρο με την απεικόνιση των γράφων, θα εκτελεστούν τα επομένα 2 παραδείγματα όπου πάλι θα εμφανιστούν τα αποτελέσματα από την εκτέλεση του αλγορίθμου (και extra η απεικόνιση των γράφων)

## 4. Εφαρμογή αλγορίθμου σε πραγματικά δεδομένα

#### 1. Εφαρμογή αλγορίθμου στο dataset ζέβρων του Grévy (Equus grevyi) στην Κένυα.

Για την εκτέλεση του αρχείου `zebras.py` πρέπει να γίνει η εγκατάσταση του dataset από [εδώ](http://konect.cc/networks/moreno_zebra) ([download link](http://konect.cc/files/download.tsv.moreno_zebra.tar.bz2)), έπειτα αποσυμπίεση του αρχείου και τέλος στην μεταβλητή file_path επικολληση του path όπου βρίσκεται το αρχείο `out.moreno_zebra_zebra` και έτσι εκτελείται το αρχείο σωστά.

#### 2. Εφαρμογή αλγορίθμου στο dataset Corporate Club Memberships όπου περιέχει πληροφορίες μελών εταιρικών στελεχών σε κοινωνικούς οργανισμούς όπως λέσχες και συμβούλια.

Για την εκτέλεση του αρχείου `corporate_club_memberships.py` πρέπει να γίνει η εγκατάσταση του dataset από [εδώ](http://konect.cc/networks/brunson_club-membership/) ([download link](http://konect.cc/files/download.tsv.brunson_club-membership.tar.bz2)), έπειτα αποσυμπίεση του αρχείου και τέλος στην μεταβλητή file_path επικολληση του path όπου βρίσκεται το αρχείο `out.brunson_club-membership_club-membership` και έτσι εκτελείται το αρχείο σωστά.



#### 3. Εφαρμογή αλγορίθμου στο dataset (google_data.py) όπου περέχει το δίκτυο υπερσυνδέσμων από σελίδες εντός των ιστότοπων της Google, π.χ. στο google.com.

Για την εκτέλεση του αρχείου `google_data.py` πρέπει να γίνει η εγκατάσταση του dataset από [εδώ](http://konect.cc/networks/cfinder-google/) ([download link](http://konect.cc/files/download.tsv.cfinder-google.tar.bz2)), έπειτα αποσυμπίεση του αρχείου και τέλος στην μεταβλητή file_path επικολληση του path όπου βρίσκεται το αρχείο `out.cfinder-google` και έτσι εκτελείται το αρχείο σωστά.

# Δεύτερο Μέρος

Ο αλγόριθμος Louvain είναι ένας αλγόριθμος κοινωνικής δικτύωσης που χρησιμοποιείται για τον εντοπισμό κοινοτήτων σε γράφους. Ο στόχος του αλγορίθμου είναι να βρει τη δομή της κοινωνικής οργάνωσης ενός δικτύου, διαχωρίζοντας τους κόμβους σε διάφορες κοινότητες ή ομάδες με βάση την αλληλεπίδραση τους.

Για την έκτελεση του αλγορίθμου χρησιμοποιήσαμε το dataset από πραγματικά δεδομένα που εξετάσαμε με τις Ζέβρες. Το αρχείο για εκτέλεση του αλγορίθμου είναι το `partitioned_graph_algorithm.py`.



License Information
-------------------

The software was developed for a  project to the Graph Technologies course of the Department of Informatics and Telematics (DIT) of the University of Athens (HUA).

## HUA Developers

#### Ioannis Mavrodimos - it22068@hua.gr
#### Christos Meidanis - it22069@hua.gr

