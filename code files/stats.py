def stats(data_list):
    """
    :param data_list: A list of dictionaries containing various attributes.
    :return: The structure of data_list with statistics about its attributes.

    Function that shows the data structure and,
    for each type  of attributes (int, str, list, bool),
    the following statistics:
     - mean, min, max, standard deviation for the int,
     - the mean of length, the longest and the shortest string for the str,
     - the percentage of True and False for the bool,
     - the list size mean, the smallest and greatest list sizes for the list
    """

    different_attributes = [[] for _ in range(len(data_list[0]))]
    different_attributes_names = [x for x in data_list[0]]
    index = 0
    for item in data_list:
        for data in item:
            different_attributes[index].append(item[data])
            index += 1
        index = 0

    stats_list = []
    for i in different_attributes:
        if isinstance(i[0], bool):
            true_count = sum(i)
            false_count = len(i) - true_count
            stats_list.append({
                'percentage true': round(true_count / len(i),2) * 100,
                'percentage false': round(false_count / len(i),2) * 100
            })
        elif isinstance(i[0], int) or isinstance(i[0], float):
            stats_list.append({
                'mean': sum(i) / len(i),
                'min': min(i),
                'max': max(i),
                'standard deviation': round((sum((x - (sum(i) / len(i))) ** 2 for x in i) / len(i)) ** 0.5,2)
            })
        elif isinstance(i[0], str):
            lengths = [len(s) for s in i]
            stats_list.append({
                'mean length': round(sum(lengths) / len(lengths),2),
                'longest': max(lengths),
                'shortest': min(lengths)
            })
        elif isinstance(i[0], list):
            sizes = [len(lst) for lst in i]
            stats_list.append({
                'mean size': round(sum(sizes) / len(sizes),2),
                'smallest size': min(sizes),
                'greatest size': max(sizes)
            })
        index += 1

    index = 0
    stats_final = []
    for i in stats_list:
        stats_final.append(list(i.items()))

    for name in different_attributes_names:
        print(f"{name.upper()}, type : {type(data_list[0][different_attributes_names[index]]).__name__}, stats : ",end="")
        for i in stats_final[index]:
            if i == stats_final[index][-1]:
                print(f"{i[0]} : {i[1]}",end="")
            else:
                print(f"{i[0]} : {i[1]}, ",end="")
        print("")
        index +=1

    print("\n")
    input("Done watching ? ")