# -*- coding: utf-8 -*-

import math
import csv
import copy
from fractions import Fraction

AGE_GRANULARITY = 10


def reidentify_patient(record_hospital):
    gender = record_hospital['gender']
    age = record_hospital['age']
    zipcode = record_hospital['zipcode']
    success = False
    data = ""
    # TODO Find the matching record in voters that has the same gender,age and zipcode
    # TODO If exactly one match found, re-identification is successful, set success_ variable to True; otherwise to False
    # TODO Save the matching voting record in a variable called record_voter

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

    # TODO implement this method using the provided VGH
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
    # TODO implement this method
    # k = ...

    k = -1 # TODO DELETE THIS LINE
    return k


def compute_distortion(levels, max_levels):
    assert len(max_levels) == len(levels)
    # TODO implement this method
    # d = ...
    print(math.modf(Fraction(1, len(max_levels)) * (Fraction(levels[0], max_levels[0]) + Fraction(levels[1], max_levels[1]) + Fraction(levels[2], max_levels[2])))[0])
    d = math.modf(Fraction(1, len(max_levels)) * (Fraction(levels[0], max_levels[0]) + Fraction(levels[1], max_levels[1]) + Fraction(levels[2],max_levels[2])))[0]

    #d = -1 # TODO DELETE THIS LINE
    return d


if __name__ == '__main__':


    with open('voters.txt') as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024))
        csvfile.seek(0)
        reader = csv.DictReader(csvfile, dialect=dialect)
        voters_records = [record for record in reader]

        #print (voters_records[0])
    # for record in voters_records:
    #    print(record['name'], record['gender'], record['age'], record['zipcode'])

    with open('hospital_records.txt') as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024))
        csvfile.seek(0)
        reader = csv.DictReader(csvfile, dialect=dialect)
        hospital_records = [record for record in reader]

        age = []

        for i in hospital_records:
            age.append(i["age"])


    print(generalize_zipcode("1170", 4))


    # Question 1

    if (reidentify_patient(hospital_records[0])):
        print("Information of the patient: {}".format(reidentify_patient(hospital_records[32])))
    else:
        print("There's no match on this patient, please try another one")

    # TODO print a list of all successfully re-identified patients with their name and disease

    # TODO print the successful re-identification rate as a percent


    # Questions 2 -> 6

    # question 5
    compute_distortion([1, 1, 2], [1, 3, 4])

    k_target = 5

    level_gender_max = -1 # TODO Use the VGH to replace with the correct value
    level_age_max =  -1 # TODO Use the VGH to replace with the correct value
    level_zipcode_max = -1  # TODO Use the VGH to replace with the correct value

    # TODO Compute each possible generalization of hospital_records and pick the optimal one as described in the exercise

    # TODO Set variables opt_level_gender, opt_level_age, opt_level_zipcode with the found optimal generalization levels
    # TODO Set variable distortion_opt with the distorsion value of the optimal generalization
    # TODO Set variable k_opt with the k-anonimity value of the optimal generalization

    # TODO Uncomment the following two lines
#    params_opt = (opt_level_gender, opt_level_age, opt_level_zipcode)
#    print('Optimal scheme (targeted k=%d): levels(gender,age,zipcode)=%s, distortion=%.2f, k=%d' % (k_target, str(params_opt), distortion_opt, k_opt))