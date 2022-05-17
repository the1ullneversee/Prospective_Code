import main
import pytest
import random
import numpy as np

def test_segment_creation():
    segment_list = [("Princes Street", "London Wall"),
                    ("Monument Station", "King William Street"),
                    ("London Bridge", "Monument Station"),
                    ("King William Street", "Princes Street")]

    desired_output = ["London Bridge", "Monument Station", "King William Street",
            "Princes Street", "London Wall"]

    output = main.segment_to_route(segment_list)

    assert output == desired_output

def test_seg_creation_mixed():
    segment_list = [("Princes Street", "London Wall"),
                    ("Monument Station", "King William Street"),
                    ("King William Street", "Princes Street"),
                     ("London Bridge", "Monument Station")]
    desired_output = ["London Bridge", "Monument Station", "King William Street",
            "Princes Street", "London Wall"]

    output = main.segment_to_route(segment_list)

    assert output == desired_output

def test_seg_creation_empty():
    segment_list = []
    desired_output = []

    output = main.segment_to_route(segment_list)

    assert output == desired_output

def test_seg_creation_no_start():
    segment_list = [("Princes Street", "London Wall"),
                    ("Monument Station", "King William Street"),
                    ("King William Street", "Princes Street"),
                     ("London Bridge", "Monument Station"),
                      ("Monument Station","London Bridge")]

    desired_output = []

    output = main.segment_to_route(segment_list)

    assert output == desired_output

def generate_numbers(n):
    i = 0

    with open('randnumbers.txt','w') as file:
        while i < n:
            num = random.randrange(0,n)
            file.write(f"{num}\n")
            i += 1
        file.close()

    #reads in as float/double
    arr = np.loadtxt('randnumbers.txt')

    #convert values to int
    arr = arr.astype('int')

    #grab the counts of unique values
    unique, counts = np.unique(arr, return_counts=True)

    #zip the count plus numbers back together
    zip_arr = zip(unique,counts)

    #sort them by the count
    s_arr = sorted(zip_arr,key=lambda x: x[1],reverse=True)
    n_arr = []
    for i in range(0,5):
        n_arr.append(s_arr[i][0])

    return 'randnumbers.txt',n_arr

def test_number_occurence():

    f_name,actual = generate_numbers(1000)
    output = main.number_occurence_finder(f_name)

    assert output == actual


