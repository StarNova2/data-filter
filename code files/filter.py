def filter(data_list, index, criteria, comparison):
    """
    :param data_list: (list) A list of dictionaries containing various attributes.
    :param index: (int) The index of the element used to filter data_list.
    :param criteria: (int) The integer used to be compared to data in order to filter it.
    :param comparison: (int) 1 for filtering out elements over criteria, 2 for filtering out elements under criteria or 3 to keep only elements equals to criteria.
    :return: The filtered elements from the list of dictionaries.

    Filters the data_list based on certain criterias.
    """
    
    new_data_list = []
    index = list(data_list[0].keys())[index]

    is_numeral = isinstance(data_list[0][index],int) or isinstance(data_list[0][index],float)
    is_bool = isinstance(data_list[0][index],bool)
    #is_str = isinstance(data_list[0][index],str)
    #is_list = isinstance(list(data_list[0].keys())[index],list)

    if comparison == 1:
        #select elements superior to criteria
        for item in data_list:
            if is_bool:
                if item[index] != criteria:
                    new_data_list.append(item)
            elif is_numeral:
                if item[index] < criteria:
                    new_data_list.append(item)
            else: #is_str or is_list
                if criteria < len(item[index]):
                    new_data_list.append(item)
                    
    elif comparison == 2:
        #select elements inferior to criteria
        for item in data_list:
            if is_bool:
                if item[index] != criteria:
                    new_data_list.append(item)
            elif is_numeral:
                if item[index] > criteria:
                    new_data_list.append(item)
            else: #is_str or is_list
                if criteria > len(item[index]):
                    new_data_list.append(item)

    elif comparison == 3:
        #select elements equals to criteria
        for item in data_list:
            if is_bool:
                if item[index] == criteria:
                    new_data_list.append(item)
            elif is_numeral:
                if item[index] == criteria:
                    new_data_list.append(item)
            else: #is_str or is_list
                if criteria == len(item[index]):
                    new_data_list.append(item)
    
    return new_data_list