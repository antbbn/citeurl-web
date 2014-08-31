import re

import mnras
import prd
import apj
import jcap
import prl
import prb
import nature

list = []
list.append(mnras.matcher)
list.append(prd.matcher)
list.append(apj.matcher)
list.append(jcap.matcher)
list.append(prl.matcher)
list.append(prb.matcher)
list.append(nature.matcher)

def match(obj, cit):
  for pattern in obj.patterns:
    result = re.search(pattern,cit,re.IGNORECASE)
    if result:
      [setattr(obj,field,result.group(field)) for field in obj.fields]
      return True
  return False
