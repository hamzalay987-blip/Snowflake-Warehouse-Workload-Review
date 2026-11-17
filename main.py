import csv
from collections import defaultdict

def run(path='data/query_history.csv'):
    agg=defaultdict(lambda:{'runs':0,'seconds':0.,'credits':0.})
    with open(path,newline='') as f:
        for r in csv.DictReader(f):
            x=agg[r['fingerprint']]; x['runs']+=1; x['seconds']+=float(r['elapsed_seconds']); x['credits']+=float(r['credits'])
    ranked=sorted(agg.items(),key=lambda x:-x[1]['credits'])
    return {'patterns':len(ranked),'highest_credit_fingerprint':ranked[0][0],'cost_by_fingerprint':{k:round(v['credits'],2) for k,v in ranked}}

if __name__ == '__main__':
    import json
    print(json.dumps(run(), indent=2))
