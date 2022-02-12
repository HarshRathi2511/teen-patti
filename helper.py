def find_duplicates(sequence):
  first_seen = set()
  first_seen_add = first_seen.add  
  duplicates = set(i for i in sequence if i in first_seen or first_seen_add(i) )
  return list(duplicates)

def countOccurrencesInList(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count  

def rm_element_from_list(lst,x):
    for ele in lst:
        lst.remove(x)
    return lst    
    