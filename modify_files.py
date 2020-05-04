

import os
import shutil
import sys
import re
from functools import cmp_to_key

def myfun(a, b):
    numa = int(re.search("\.([0-9]+)\.",a).group(1))
    numb = int(re.search("\.([0-9]+)\.",b).group(1))
    return numa - numb

if __name__ == '__main__':

    dirs = list()
    with open('content.txt','r',encoding='utf-8') as f:
        for line in f:
                dirs.append(line.strip())
    srcFiles = list()
    count = 0
    sum = 0;
    for i in range(9,13):
        # srcFiles[count].append(os.listdir("./%s"%(i)))
        tmp = os.listdir("./%s"%(i))
        sum += len(tmp)
        srcFiles.append(tmp)
        # count += 1

    # dst = list()
    # #sort
    # for i in range(4):
    #     srcFiles[i] = sorted(srcFiles[i],key=cmp_to_key(myfun))


    # count = 0
    for i in range(4):
        for file in srcFiles[i]:
            os.rename("./%s/%s"%(i+9,file),"./%s/%s.mp4"%(i+9,file))
            # count += 1
            # print(file)
