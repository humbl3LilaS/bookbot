from time import clock_getres


def get_word_count(text):
    return len(text.split())


def get_word_occurrence(text):
    occurrence_dic = {}
    words_list = list(text.lower())
    for word in words_list:
        if word in occurrence_dic:
            occurrence_dic[word] = occurrence_dic[word] + 1
        else:
            occurrence_dic[word] = 1

    return occurrence_dic


def get_count(word_dic):
    return word_dic["count"]


def get_sort_words(raw_dic):
    result = []
    for word in raw_dic:
        result.append({
            "character": word,
            "count": raw_dic[word]
        })

    result.sort(key=get_count, reverse=True)
    return result
