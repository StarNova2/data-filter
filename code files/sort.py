def sort_function(data_list,index = 0,sort_key = 0):
    """
    :param data_list: A list of dictionaries containing various attributes.
    :param index: The index of the attribute to sort by.
    :param sort_key: 0 to sort by ascending order, 1 for descending order.
    :return: The sorted list of dictionaries.

    Function to sort the data_list based on certain criteria.
    """
    sorted_list = sorted(data_list, key=lambda x: x[list(x.keys())[index]], reverse=bool(sort_key))
    return sorted_list

#print(sort_function(goty_list, 1, 0))  # Example usage: sort by title in ascending order from goty_list