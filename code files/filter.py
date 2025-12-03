def filter(data_list, index, comparison, criteria):
    """
    :param data_list: A list of dictionaries containing various attributes.
    :param criteria: The index of the element used to filter data_list.
    :return: The filtered elements from the list of dictionaries.

    Filters the data_list based on certain criteria.
    """
    
    new_data_list = []
    is_numeral = isinstance(data_list[0][index],int) or isinstance(data_list[0][index],float)
    is_str = isinstance(data_list[0][index],str)
    is_bool = isinstance(data_list[0][index],bool)
    is_list = isinstance(data_list[0][index],list)

    if comparison == '1':
        #selectionne les éléments inférieurs à criteria
        for item in data_list:
            if is_numeral:
                if item[index] < criteria:
                    new_data_list.append(item)
            elif is_str:
                if criteria.lower() < item[index].lower():
                    new_data_list.append(item)
            elif is_bool:
                if item[index] != criteria:
                    new_data_list.append(item)
            else: #is_list
                if criteria < len(item[index]):
                    new_data_list.append(item)
                    
    elif comparison == '2':
        #selectionne les éléments supérieurs à criteria
        for item in data_list:
            if is_numeral:
                if item[index] > criteria:
                    new_data_list.append(item)
            elif is_str:
                if criteria.lower() < item[index].lower():
                    new_data_list.append(item)
            elif is_bool:
                if item[index] != criteria:
                    new_data_list.append(item)
            else: #is_list
                if criteria > len(item[index]):
                    new_data_list.append(item)

    elif comparison == '3':
        #selectionne les éléments égaux à criteria
        for item in data_list:
            if is_numeral:
                if item[index] == criteria:
                    new_data_list.append(item)
            elif is_str:
                if criteria.lower() == item[index].lower():
                    new_data_list.append(item)
            elif is_bool:
                if item[index] == criteria:
                    new_data_list.append(item)
            else: #is_list
                if criteria == len(item[index]):
                    new_data_list.append(item)
    
    return new_data_list
    