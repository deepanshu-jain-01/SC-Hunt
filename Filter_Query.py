import json
import random

def filter(data, loc, job_type):

    loc_len, job_type_len = len(loc), len(job_type) 

    filtered = {}

    if loc_len==0 and job_type_len==0:
        return data

    elif loc_len==0 and job_type_len!=0:

        for src in job_type:
            for k,v in data.items():
                if src in v['job_type']:
                    filtered.update({k:v})

        return filtered

    elif job_type_len==0 and loc_len!=0:

        for src in loc:
            for k,v in data.items():
                print(src,"=>",v['location'])
                if src in v['location']:
                    filtered.update({k:v})

        return filtered

    else:

        for src in loc:
            for k,v in data.items():
                if src in v['location']:
                    filtered.update({k:v})

        data = filtered

        filtered = {}

        for src in job_type:
            for k,v in data.items():
                if src in v['job_type']:
                    filtered.update({k:v})

        return filtered

def sorting(data, field_name, rev_flag):

    sort_data = {k:v for k, v in sorted(data.items(), key=lambda item: item[1][field_name], reverse=rev_flag)}

    return sort_data

def search(data, search_term):

    filtered = {}

    for k,v in data.items():
        if search_term.lower() in v['job_title'].lower():
            filtered.update({k:v})

    return filtered

def shuffle(data):
    
    shuf_data = list(data.items())
    random.shuffle(shuf_data)

    #page_data = [dict(data[i:i+10]) for i in range(0, len(data), 10)]
  
    return dict(shuf_data)
