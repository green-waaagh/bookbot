def get_num_words(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        count=len(file_contents.split())
        return count
    
def get_num_characters(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        dict = {}
        for ch in file_contents.lower():
            if ch not in dict:
                dict[ch] = 1
                #add ch to key in dict with count 1
            else:
                dict[ch] += 1
                #add ch_count +1
        return dict

def sort_on(items):
    return items["num"]

def sort_list(filepath):
    list_of_dict = []
    dict = get_num_characters(filepath)
    for k, v in dict.items():
        dict_ext = {'char': k, 'num': v}
        list_of_dict.append(dict_ext)
    list_of_dict.sort(key=sort_on, reverse=True)
    letters_only = []
    for item in list_of_dict:
        if item["char"].isalpha():
            letters_only.append(item)
    return letters_only