
import uuid
""" for loaded json enumerate it to fit auto increment style ids """
def enumerate_json(json):
  o = dict() 
  c = 0
  for i in json:
    o[c] = i
    c+=1 

  return o



