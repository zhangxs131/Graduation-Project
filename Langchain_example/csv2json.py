import pandas as pd
import sys



df=pd.read_csv(sys.argv[1])
df.to_json(sys.argv[2],force_ascii=False,indent=4)