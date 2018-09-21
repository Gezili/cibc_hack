import os
import sys
import pandas
from pathlib import Path

directory = str(Path(__file__).parents[0])
sys.path.append(directory)

#Put the CSV in the same directory as this .py file
#We work to build a list of all unique providers, unique procedures

def build_list_providers():
    
    list = pandas.read_csv(directory + r'/claims_final.csv')
    procedure_list = list.ix[:,6]
    procedure_list_unique = []
    for i, id in enumerate(procedure_list):
        if id not in procedure_list_unique:
            procedure_list_unique.append(id)
            
    #for id in procedure_list_unique:
    #   with open(directory + r'\unique_procedures.csv', 'a') as f:
    #       f.write(str(id) + ',\n')
    
    return procedure_list_unique
    
def build_list_costs():
    
    list = pandas.read_csv(directory + r'/claims_final.csv')
    procedure_list_unique = build_list_providers()
    procedure_list = list.ix[:,6]
    costs = list.ix[:,7]
    
    cost_arr = []
    for i in range(len(procedure_list_unique)):
        cost_arr.append([])
    
    for i, id in enumerate(costs):
        cost_arr[procedure_list_unique.index(procedure_list[i])].append(id)

    with open(directory + r'\procedure_cost.csv', 'a') as f:
        for i, elem in enumerate(cost_arr):
            f.write(str(procedure_list_unique[i]) + ',')
            for cost in elem:
                f.write(str(cost) + ',')
            f.write('\n')
            
    return procedure_list_unique, cost_arr
            
    
    