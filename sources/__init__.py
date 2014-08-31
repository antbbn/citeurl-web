import re

import mnras
import prd
import apj
import jcap

list = []
list.append(mnras.matcher)
list.append(prd.matcher)
list.append(apj.matcher)
list.append(jcap.matcher)

def match(obj, cit):
  for pattern in obj.patterns:
    result = re.search(pattern,cit,re.IGNORECASE)
    if result:
      [setattr(obj,field,result.group(field)) for field in obj.fields]
      return True
  return False
