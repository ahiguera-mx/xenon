import numpy as np
from utilix.rundb import xent_collection

db = xent_collection('runs')
osg_all_dtypes = ['lone_hits', 'merged_s2s', 'peaklet_classification', 'peak_basics', 
                  'distinct_channels', 'event_basics', 'corrected_areas', 'energy_estimates', 'event_info',
                  'event_pattern_fit', 'event_positions', 'peak_positions_gcn', 'peak_positions_cnn', 
                  'peak_proximity', 'peak_positions_mlp']

 
r = db.find_one({'number' : 50025 })
for d in r['data']:
    if d['type'] in osg_all_dtypes and d['host'] == 'rucio-catalogue':
        print('================================')
        print(d)
        print('\n')
       
