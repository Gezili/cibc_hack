import os
import sys
import pandas
from pathlib import Path
import numpy as np

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

    '''
    with open(directory + r'\procedure_cost.csv', 'a') as f:
        for i, elem in enumerate(cost_arr):
            f.write(str(procedure_list_unique[i]) + ',')
            for cost in elem:
                f.write(str(cost) + ',')
            f.write('\n')
    '''
    list_mean = []
    list_std = []
    num_elements = []
    
    for elem in cost_arr:
        list_mean.append(np.mean(elem))
        list_std.append(np.std(elem))
        num_elements.append(len(elem))
        
    with open(directory + r'\procedure_stats.csv', 'a') as f:
        for i in range(len(procedure_list_unique)):
            f.write(str(procedure_list_unique[i]) + ',')
            f.write(str(list_mean[i]) + ',')
            f.write(str(list_std[i]) + ',')
            f.write(str(num_elements[i]) + '\n')
            
def build_provider_info():
    
    list = pandas.read_csv(directory + r'/claims_final.csv')
    provider_list = list.ix[:,2]
    provider_list_unique = []
    for i, id in enumerate(provider_list):
        if id not in provider_list_unique:
            provider_list_unique.append(id)
    
    with open(directory + r'\unique_providers.csv', 'a') as f:        
        for id in provider_list_unique:
           f.write(str(id) + ',\n')
    
    return provider_list_unique

def export_unique_lists():
    col_Names=["Patient_Family_ID", "Family_Member_ID", "Provider_ID", "Provider_Type", "State_Code", "Date_of_Service", "Procedure_Code","Dollar_Claimed"]
    data = pandas.read_csv("claims_final.csv", names = col_Names)
    for name in col_Names:
        unique_list = data[name].unique()
        df = pandas.DataFrame(sorted(unique_list), columns = [name])
        file_name = name+"_unique"+".csv"
        df.to_csv(file_name, index=False, header=False)
    
    