#!/usr/bin/env python
# coding: utf-8

# In[4]:


import argparse
import re
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("--infile", "-i", type=str, help="CSV for dataset to expand",
                    required=True)
args = parser.parse_args()

for topic in ["lockdowns", "masking and distancing", "vaccination"]:
    df = pd.read_csv(args.infile)
    cols = df.columns
    for col in cols:
        if "annotation" in col:
            df[col] = (df[col].notna() & df[col].str.contains(topic))
    new_fn = re.sub(r"\.csv$", f"_{topic.replace(' ', '_')}.csv", args.infile)
    df.to_csv(new_fn, index=False)


# In[ ]:





# In[ ]:




