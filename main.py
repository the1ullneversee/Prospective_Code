import time
import os
import numpy as np
import random
def segment_to_route(trip_segments):
    
    starts = {}
    ends = {}

    #check for mal input
    if len(trip_segments) <= 1:
        return []

    #for each 
    for segment in trip_segments:
        
        start = segment[0]
        end = segment[1]

        #gather the start to end segment, then the other way around.
        starts[start] = end
        ends[end] = start


    #convert both start stations and end stations 
    s_stops = set.difference(set(starts.keys()),set(ends.keys()))
    #if we have no starts, or more than 1, throw back empty.
    if len(s_stops) != 1:
        return []

    station = s_stops.pop()

    stop_list = [station]

    #O(n)
    while station != "":
        station = starts.get(station,"")
        if station != "":
            stop_list.append(station)

    return stop_list


def number_occurence_finder(filename):
    #check for invalid filename
    if not os.path.isfile(filename):
        print("invalid")
        return []
    
    numbers = {}
    with open(filename,'r') as file:
        num = file.readline()
        while num:

            #try added so that we can cast the line item to an int, to check it actually is a number
            try:
                num = num.strip('\n')
                int(num)
            except:
                num = ""

            #if it is a number then go ahead and calculate with it.
            if num != "":    
                numbers[num] = numbers.get(num,0) + 1
                num = file.readline()
            

    #sort the dictionary and then use splice to cut up to the top 5
    numbers = sorted(numbers.items(),key=lambda x: x[1],reverse=True)[:5]

    #print out the top 5
    ret_arr = []
    for n in numbers:
        print(n[0])
        ret_arr.append(n[0])
        
    #for the purpose of testing
    return ret_arr


