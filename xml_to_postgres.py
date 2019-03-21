import re
from sqlalchemy import create_engine
from os import listdir
import pandas as pd 
from tqdm import tqdm
engine = create_engine('postgresql://username:password@localhost/wikipedia')
files = [x for x in listdir('.') if re.findall('^x..',x) and x!='xaa']

for f_name in tqdm(files):
    f = open(f_name)
    data = f.read()
    pages = re.findall('<page.*?</page',data,re.DOTALL)
    lst = []
    for page in pages:
        resp = re.findall("<(text)(.*?)</text|<(base)(.*?)</base|<(case)(.*?)</case|<(comment)(.*?)</comment|<(dbname)(.*?)</dbname|<(format)(.*?)</format|<(id)(.*?)</id|<(ip)(.*?)</ip|<(model)(.*?)</model|<(ns)(.*?)</ns|<(parentid)(.*?)</parentid|<(restrictions)(.*?)</restrictions|<(sha1)(.*?)</sha1|<(sitename)(.*?)</sitename|<(timestamp)(.*?)</timestamp|<(title)(.*?)</title|<(username)(.*?)</username",page,re.DOTALL)
        dct = {}
        temp = []

        for ix in resp:
            for iy in ix:
                if iy:
                    temp.append(iy)
            dct[temp[0]]=re.sub('^>','',' '.join(temp[1:]))
            temp = []
        lst.append(dct)


    df = pd.DataFrame(lst)

    df.to_sql('wiki',engine,if_exists='append')
