# -*- coding: utf-8 -*-

import math
import csv
import copy
from collections import OrderedDict
from fractions import Fraction

AGE_GRANULARITY = 10


def reidentify_patient(record_hospital):
    gender = record_hospital['gender']
    age = record_hospital['age']
    zipcode = record_hospital['zipcode']
    success = False
    data = ""

    with open('voters.txt') as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024))
        csvfile.seek(0)
        reader = csv.DictReader(csvfile, dialect=dialect)

        # Check if the data matches the records of voters
        for record in reader:
            if gender == record["gender"] and age == record["age"] and zipcode == record["zipcode"]:
                success=True
                data = record["name"] + ": " + record_hospital["condition"]

    if success:
        return True, data
    else:
        return False



def generalize_gender(gender: str, level: int):
    assert (type(level) is int and level >= 0)
    assert (gender in ['male', 'female'])

    if level == 0:
        return gender
    else:
        return '*'


def generalize_age(age: int, level: int):
    assert (type(level) is int and level >= 0)
    assert (type(age) is int and age > 0)

    if level == 0:
        return age
    elif 0 < level < 3:
        granularity = AGE_GRANULARITY * level
        age_ = granularity * math.floor(age / granularity)
        return '[%d-%d[' % (age_, age_ + granularity)
    else:
        return '*'


#Question 3
def generalize_zipcode(zipcode: str, level: int):
    assert (type(level) is int and level >= 0)
    assert (type(zipcode)) is str and zipcode != ""

    if level == 0:
        return zipcode

    elif 0 < level <= len(zipcode):
        ast = ""
        i=0
        while i < level:
            i += 1
            ast += "*"
        zipcode = zipcode[:-level]+ast
        return zipcode
    else:
        return "Error: define another value for level"




def generalize_record(record, level_gender, level_age, level_zipcode):
    record_ = copy.deepcopy(record)
    record_['gender'] = generalize_gender(record['gender'], level_gender)
    record_['age'] = generalize_age(int(record['age']), level_age)
    record_['zipcode'] = generalize_zipcode(record['zipcode'], level_zipcode)
    return record_


def generalize_database(records, level_gender, level_age, level_zipcode):
    # This method generalizes the entire hospital_records
    return [generalize_record(record, level_gender, level_age, level_zipcode) for record in records]


def compute_anonymity_level(records, quasi_identifiers):
    n=0
    k = []
    nr = [] #nr = New records = liste épurée

    age = []
    zipcode = []

    #Read records
    for i in range (0, len(records)):
        new_records = OrderedDict()
        for ii in range (len(quasi_identifiers)):
            v = str (quasi_identifiers[ii])
            new_records[quasi_identifiers[ii]] = records.__getitem__(i)[v]
        nr.append(new_records)

    # Get all the keys
    for i in nr:
        l = i.keys()
    l2 = list(l)

    # Lecture de records
    for i in range (0, len (nr)):
        #print(len(nr))
        # Comparaison avec les autres records (new records)
        for ii in range (0, len (l2)):
            n = 0
            #print ("{} is {}".format(l2[ii], nr.__getitem__(i)[l2[ii]]))
            for x in range(0, len(nr)):
                # Cette boucle permet de comparer
                temp_n = 0
                for ii in range(0, len(l2)):
                    # On récupère uniquement les valeurs identiques
                    if (l2[ii] == "zipcode"):
                        zipcode = nr.__getitem__(i)[l2[ii]]
                    if (l2[ii] == "age"):
                        age = nr.__getitem__(i)[l2[ii]]
                    if (l2[ii] == "gender"):
                        gender = nr.__getitem__(i)[l2[ii]]

                    if nr.__getitem__(i)[l2[ii]] == nr.__getitem__(x)[l2[ii]]:
                        temp_n+=1
                        if temp_n == 3:
                            n+=1
        k.append(n)

    # Retourne la valeur minimale de k
    return min(k)


def compute_distortion(levels, max_levels):
    assert len(max_levels) == len(levels)
    d = math.modf(Fraction(1, len(max_levels)) * (Fraction(levels[0], max_levels[0]) + Fraction(levels[1], max_levels[1]) + Fraction(levels[2],max_levels[2])))[0]
    return d


if __name__ == '__main__':

    with open('voters.txt') as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024))
        csvfile.seek(0)
        reader = csv.DictReader(csvfile, dialect=dialect)
        voters_records = [record for record in reader]


    with open('hospital_records.txt') as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024))
        csvfile.seek(0)
        reader = csv.DictReader(csvfile, dialect=dialect)
        hospital_records = [record for record in reader]
        print(hospital_records)
        age = []
        for i in hospital_records:
            age.append(i["age"])


    # Question 1

    #Patient 12 pris aléatoirement - Il est possible de réidentifier un autre patient en modifiant l'index de la liste hospital_records
    if (reidentify_patient(hospital_records[12])):
        print ("**** Question 1 ****")
        print("Information of the patient: {}".format(reidentify_patient(hospital_records[12])))
        print ("********\n")
    else:
        print("There's no match on this patient, please try another one")

    # Question 3

    # Generalization of a random patient (12)
    print("**** Question 3 ****")
    print (generalize_record(hospital_records[12],1, 1, 2))
    print("********\n")

    # Question 4
    # Anonymity level of a random data set
    # Adding random values in order to compute anonymity level
    liste = []
    liste.append(hospital_records[19])
    liste.append(hospital_records[1])
    liste.append(hospital_records[12])
    liste.append(hospital_records[4])

    qid = ["gender", "age", "zipcode"]

    print("**** Question 4 ****")
    print("The Anonymity level is {}".format(compute_anonymity_level(liste, qid)))
    print("********\n")

    #Question 5

    print("**** Question 5 ****")
    print("The Distortion with the specific values [1, 1, 2] and maximum values [1, 3, 4] is {}".format(compute_distortion([1, 1, 2], [1, 3, 4])))
    print("********\n")

    # Questions 6

    k_target = 5

    level_gender_max = 1
    level_age_max =  3
    level_zipcode_max = 4

    level_gender_opt = 1
    level_age_opt = 1
    level_zipcode_opt = 2

    params_max = (level_gender_max, level_age_max, level_zipcode_max)
    min_d = []
    min_k = []
    data_opt = []

    print("**** Question 6 ****")
    print ("Computing, please wait...")
    for i in range(0,level_gender_max+1):
        for j in range(0,level_age_max+1):
            for m in range(0,level_zipcode_max+1):
                params_opt = (i,j,m)
                #print (params_opt)
                k_opt = compute_anonymity_level(generalize_database(hospital_records, i, j, m), qid)
                #print('Optimal scheme (targeted k=%d): levels(gender,age,zipcode)=%s, distortion=%.2f, k=%d' % (k_target, str(params_opt), compute_distortion(params_opt, params_max), k_opt))
                if 5 < k_opt < 400:
                    data_opt.append('Optimal scheme (targeted k=%d): levels(gender,age,zipcode)=%s, distortion=%.2f, k=%d' % (k_target, str(params_opt), compute_distortion(params_opt, params_max), k_opt))
                    min_d.append(compute_distortion(params_opt, params_max))

    index = min_d.index(min(min_d))
    print("{}".format(data_opt[index]))
