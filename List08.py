def main(list1):
    """
    A list of ones and zeros, five in length, is given. replace one with True, replace zeros with False.
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
            list2.append(False)
        a+=1        
    return list2
print(main([1,0,1,0]))    