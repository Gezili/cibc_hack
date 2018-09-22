import numpy as np
import pandas as pd
from collections import defaultdict

provider_files = ['count_model.csv']
weights = [100]

provider_scores = defaultdict(int)
for file, weight in zip(provider_files, weights):
    with open(file) as f:
        for line in f:
            provider, rank = line.split(',')
            provider_scores[int(provider)] += 1 / (int(rank) + 1) / weight

providers = np.array(list(provider_scores.values()))
sorted_args = providers.argsort()
ranked_providers = np.flip(np.array(list(provider_scores.keys()))[sorted_args], axis=0)

# This is file 1, i.e. the result
with open('outlying-providers.csv', 'w') as f: 
    for i, provider_id in enumerate(ranked_providers):
        f.write(str(provider_id) + ',' + str(i+1) + '\n')
        
        

claim_files = []
claim_scores = defaultdict(int)
for file, weight in zip(claim_files, weights):
    with open(file) as f:
        for line in f:
            claim, rank = line.split(',')
            claim_scores[int(claim)] += int(rank) * weight
ordered_claim_scores = [claim_scores[i] for i in range(len(claim_scores))]

# Get the top 100 for each provider type, this is the result for file 2
final_claims = pd.read_csv('claims_final.csv', header=None, names=['fam id', 'fam member id', 'provider id', 'provider type', 'state', 'date', 'procedure code', 'amount'])
final_claims['score'] = ordered_claim_scores
provider_types = final_claims.groupby('provider type').count()['amount'].keys()
with open('outlying-provider-types.csv', 'w') as f:
    for provider_type in provider_types:
        nlargest = final_claims[final_claims['provider type'] == provider_type].nlargest(100, 'score')
        nlargest = nlargest.reindex(columns=['fam id', 'fam member id', 'provider id', 'date', 'provider type'])
        nlargest['outlier rank'] = np.arange(len(nlargest))
        nlargest.to_csv(f, header=False, index=False)
    