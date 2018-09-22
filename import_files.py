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

def find_provider_patients():
    
    provider_list = pandas.read_csv(directory + r'/Provider_ID_Unique.csv').ix[:,0]
    provider_list_unique = [provider_list[i] for i in range(len(provider_list))]

    provider_list = pandas.read_csv(directory + r'/Provider_ID_Unique.csv')
    provider_list['provider id'].groupby('provider id').count()

    sum_providers = np.zeros(len(provider_list_unique), dtype = int)
    #return sum_providers
    prov_list = pandas.read_csv(directory + r'/claims_final.csv').ix[:,2]
    #prov_list = [list[i] for i in range(len(list))]
    for provider in prov_list:
        sum_providers[provider_list_unique.index(provider)] += 1
    return sum_providers

def build_provider_relationships():
    '''
    list = pandas.read_csv(directory + r'/claims_final.csv')
    provider_list_unique = pandas.read_csv(directory + r'/unique_providers.csv').ix[:,0]
    procedure_stats = pandas.read_csv(directory + r'/procedure_stats.csv')
    
    provider_id = list.ix[:,2]
    provider_type = list.ix[:,3]
    cost = list.ix[:,7]
    
    id = procedure_stats.ix[:,0]
    mean = procedure_stats.ix[:,1]
    std = procedure_stats.ix[:,2]
    
    for i in range(len(provider_list_unique)):
        cost_arr.append([])
        
    for i, entry in enumerate():
        
        abs_diff = abs(
        
        cost_arr[provider_list_unique.index(provider_list[i])].append([
            
        
        ])
    '''
    pass
    
def find_duplicate_providers():
    
    data = pandas.read_csv(directory + r"\claims_final.csv")
    duplicates = data.duplicated()
    
    provider_list_before = pandas.read_csv(directory + r'/Provider_ID_Unique.csv').ix[:,0]
    provider_list = [provider_list_before[i] for i in range(len(provider_list_before))]
    provider_id = data.ix[:,2]
    duplicate_ids = []
    for i in range(len(data)):
        if duplicates[i] == True:
            duplicate_ids.append(provider_id[i])
    #print(duplicate_ids)
    sum_providers = np.zeros(len(provider_list), dtype = int)
    
    for provider in duplicate_ids:
        sum_providers[provider_list.index(provider)] += 1
    
    with open(directory + r'\procedure_duplicates.csv', 'a') as f:
        for i in range(len(duplicate_ids)):    
            f.write(str(provider_list[i]) + ',')
            f.write(str(sum_providers[i]) + '\n')
    
    return sum_providers
    
def find_normalized_providers():
    
    data_absolute = pandas.read_csv(directory + r"/group_by_provider.csv")
    data_duplicates = pandas.read_csv(directory + r"/procedure_duplicates.csv")
    
    #return data_absolute.ix[:,0], data_duplicates.ix[:,0]
    provider_id = data_absolute.ix[:,0]
    provider_count = data_absolute.ix[:,1]
    provider_duplicates = data_duplicates.ix[:,1]

    percentage_duplicates = []
    with open(directory + r'\procedure_duplicates_percentage.csv', 'a') as f:
        for i in range(len(provider_count)):
            percentage_duplicates.append((provider_duplicates[i]/provider_count[i], provider_id[i]))
            
            f.write(str(provider_id[i]) + ',')
            f.write(str(provider_duplicates[i]/provider_count[i]) + '\n')
            
    percentage_duplicates.sort(reverse = True)
    
    with open(directory + r'\procedure_duplicates_sorted.csv', 'a') as f:
        for elem in percentage_duplicates:
            f.write(str(elem[1]) + ',')
            f.write(str(elem[0]) + '\n')
        
    return percentage_duplicates
    
def process_normals():
    
    data_z = pandas.read_csv(directory + r"/z_scores.csv")
    provider_id = data_z.ix[:,0]
    z_values = data_z.ix[:,1]
    
    with open(directory + r'\provider_mean_std.csv', 'a') as f:
        for i, provider in enumerate(provider_id):
            abs_mean = -1
            data_var = -1
            data = z_values[i].split(',')
            if len(data) > 0:
    
                data[0] = data[0][1:]
                data_replace = data[len(data) - 1]
                data[len(data) - 1] = data_replace[:len(data_replace) - 1]
                data = [float(data[i]) for i in range(len(data) - 1)]
                
                data_var = np.var(data)
                abs_mean = 0
                for i in range(len(data)):
                    abs_mean += abs(data[i])
                try:
                    abs_mean = abs_mean/len(data)
                except ZeroDivisionError:
                    abs_mean = -1
                    data_var = -1
            f.write(str(provider) + ',')
            f.write(str(data_var) + ',')
            f.write(str(abs_mean) + '\n')
            
def find_normalized_euclidean_distances():
    
    data_eu = pandas.read_csv(directory + r"/mean_euclidean_distance.csv")
    prov_id = data_eu.ix[:,0]
    distances = data_eu.ix[:,1]
    
    data_orig = pandas.read_csv(directory + r"/provider_mean_std.csv")
    find_zeros = data_orig.ix[:,1]
    
    data_assembled = [(distances[i], prov_id[i]) for i in range(len(prov_id))]
    
    for i in range(len(data_orig)):
        if find_zeros[i] < 0:
            data_assembled[i] = (0,prov_id[i])
    
    data_assembled.sort(reverse = True)
    
    with open(directory + r'/final_euclidean_distance_sorted.csv', 'a') as f:
        for elem in data_assembled:
            f.write(str(elem[1]) + ',')
            f.write(str(elem[0]) + '\n')
            
def generate_list_for_chris():
    data_eu = pandas.read_csv(directory + r"/final_euclidean_distance_sorted.csv")
    data_of_interest = data_eu.ix[:,0].tolist()
    with open(directory + r'/zili_predictions.csv', 'a') as f:
        for i, elem in enumerate(data_of_interest):
            f.write(str(elem) + ',')
            f.write(str(i) + '\n')
    
def generate_duplicates_chris():
    data_eu = pandas.read_csv(directory + r"/procedure_duplicates_sorted.csv")
    data_of_interest = data_eu.ix[:,0].tolist()
    with open(directory + r'/dupe_predictions.csv', 'a') as f:
        for i, elem in enumerate(data_of_interest):
            f.write(str(elem) + ',')
            f.write(str(i) + '\n')
            


def sum_cost():
    data = pandas.read_csv(directory + r"\claims_final.csv")
    cost = data.ix[:,7]
    money = np.sum(cost) + 707.08
    return money
