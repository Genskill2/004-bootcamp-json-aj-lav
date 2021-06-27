import json

def load_journal(file_name):
    fh = open(file_name,'r')
    data = json.loads(fh.read())
    return data
def compute_phi(file_name,event):
    n_l_,n_o_,n__l,n__o,n_ll,n_oo,n_lo,n_ol = 0,0,0,0,0,0,0,0
    data = loads_json(file_name)
    for entries in data:
        r1 = event in entries['events']
        r2 = entries['squirrel']
        if r1:
            n_l_+=1
        else:
            n_o_+=1
        if r2:
            n__l+=1
        else:
            n__o+=1
        if r1 and r2:
            n_ll+=1
        elif not r1 and not r2:
            n_oo+=1
        elif r1 and not r2:
            n_lo+=1
        else:
            n_ol+=1
    num = ((n_ll*n_oo)-(n_lo*n_ol))
    den = (n_l_ * n_o_ * n__l * n__o)**0.5
    val = num/den
    return event,val
def compute_correlations(file_name):
    journal = load_journal(file_name)
    events = list()
    corr = dict()
    for entries in  journal:
        for event in entries['events']:
            if event not in events:
                events.append(event)
                key,val = compute_phi(file_name,event)
                corr[key] = val
    return corr
def diagnose(file_name):
    ret = compute_correlations(file_name)
    dic = dict()
    for k,v in ret.items():
        dic[v] = k
        
    l = sorted(dic)
    max_val, min_val = l[-1],l[0]  
    return dic[max_val],dic[min_val]

