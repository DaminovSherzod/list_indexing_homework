def main(list1):
    """
    A list of units and zeros with a length of five is given. Replace one with True.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    a = 0
    list2 = []
    while a<len(list1):
        if list1[a]==1:
            list2.append(True)
        else:
            list2.append(0)
        a+=1        
    return list2
print(main([1,0,1,0]))    