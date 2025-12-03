goty_list = [
    {
        "year": 2010,
        "title": "Red Dead Redemption",
        "publisher": "Rockstar Games",
        "played": True
    },
    {
        "year": 2011,
        "title": "The Elder Scrolls V: Skyrim",
        "publisher": "Bethesda Softworks",
        "played": False
    },
    {
        "year": 2012,
        "title": "The Walking Dead",
        "publisher": "Telltale Games",
        "played": False
    },
    {
        "year": 2013,
        "title": "Grand Theft Auto V",
        "publisher": "Rockstar Games",
        "played": True
    },
    {
        "year": 2014,
        "title": "Dragon Age: Inquisition",
        "publisher": "Electronic Arts",
        "played": False
    },
    {
        "year": 2015,
        "title": "The Witcher 3: Wild Hunt",
        "publisher": "CD Projekt",
        "played": True
    },
    {
        "year": 2016,
        "title": "Overwatch",
        "publisher": "Blizzard Entertainment",
        "played": True
    },
    {
        "year": 2017,
        "title": "The Legend of Zelda: Breath of the Wild",
        "publisher": "Nintendo",
        "played": True
    },
    {
        "year": 2018,
        "title": "God of War",
        "publisher": "Sony Interactive Entertainment",
        "played": True
    },
    {
        "year": 2019,
        "title": "Sekiro: Shadows Die Twice",
        "publisher": "Activision",
        "played": False
    },
    {
        "year": 2020,
        "title": "The Last of Us Part II",
        "publisher": "Sony Interactive Entertainment",
        "played": False
    },
    {
        "year": 2021,
        "title": "It Takes Two",
        "publisher": "Electronic Arts",
        "played": True
    },
    {
        "year": 2022,
        "title": "Elden Ring",
        "publisher": "Bandai Namco Entertainment",
        "played": False
    },
    {
        "year": 2023,
        "title": "Baldur's Gate 3",
        "publisher": "Larian Studios",
        "played": False
    },
    {
        "year": 2024,
        "title": "Astro Bot",
        "publisher": "Sony Interactive Entertainment",
        "played": False
    }
]

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
    index = 0
    for item in data_list:
        for data in item:
            different_attributes[index].append(item[data])
            index += 1
        index = 0

    stats_dict = {}
    for i in different_attributes:
        if isinstance(i[0], bool):
            true_count = sum(i)
            false_count = len(i) - true_count
            stats_dict[index] = {
                'percentage_true': round(true_count / len(i),2) * 100,
                'percentage_false': round(false_count / len(i),2) * 100
            }
        elif isinstance(i[0], int) or isinstance(i[0], float):
            stats_dict[index] = {
                'mean': sum(i) / len(i),
                'min': min(i),
                'max': max(i),
                'std_dev': round((sum((x - (sum(i) / len(i))) ** 2 for x in i) / len(i)) ** 0.5,2)
            }
        elif isinstance(i[0], str):
            lengths = [len(s) for s in i]
            stats_dict[index] = {
                'mean_length': round(sum(lengths) / len(lengths),2),
                'longest': max(lengths),
                'shortest': min(lengths)
            }
        elif isinstance(i[0], list):
            sizes = [len(lst) for lst in i]
            stats_dict[index] = {
                'mean_size': round(sum(sizes) / len(sizes),2),
                'smallest_size': min(sizes),
                'greatest_size': max(sizes)
            }
        index += 1

    # IL RESTE A FAIRE LA PARTIE AFFICHAGE
    
    """for i in different_attributes:
        print(i)
    for i in stats_dict:
        print(stats_dict[i])"""

            
stats(goty_list)