import re
import os
import operator
import lxml.html as LH
import xml.etree.ElementTree as ET
from pathlib import Path

# Paths
MAIN_DIR = Path(f"{os.path.dirname(os.path.realpath(__file__))}").parent.parent
CORE_DIR = Path(f"{MAIN_DIR}/core")
FILES_DIR = Path(f"{MAIN_DIR}/files")
DATASETS_DIR = Path(f"{MAIN_DIR}/datasets")

"""Top 10 most viwed post"""


def top_view_mapper() -> list:
    """This function reads a .xml file, searches for "post id" and "post view count" and 
    appends these values in a dictionary within a list of dictionaries.

    Returns:
        list: List of dictionaries with format {"post_id": post_id, "view_count": view_count}. 
    """
    mytree = ET.parse(f"{DATASETS_DIR}/posts.xml")
    # Instance of the root tree.
    myroot = mytree.getroot()
    top_limit01 = len(myroot)
    post_id = None
    view_count = None
    KEY_VALUE_LIST = []
    for row in range(0, top_limit01):
        # Finding elementes.
        try:
            post_id = int(myroot[row].attrib["Id"])
            view_count = int(myroot[row].attrib["ViewCount"])
        except ValueError:
            continue
        KEY_VALUE_LIST.append(
            {"post_id": post_id,
             "view_count": view_count}
        )

    # Sort list by "view_count".
    KEY_VALUE_LIST = sorted(
        KEY_VALUE_LIST, key=operator.itemgetter("view_count"), reverse=True)

    # Get top.
    POST_VIEW_COUNT_LIST = KEY_VALUE_LIST[:10]

    return POST_VIEW_COUNT_LIST


def top_view_calculator(key_value_list: list) -> object:
    """This function iter through the key_value_list and 
    find the top 10 most viewed post. 

    Args:
        key_value_list (list): Sorted ascending list of dictionaries with format: 
        {"post_id": post_id, "view_count": view_count}.

    Returns:
        object: Text file with top 10 most viewed posts.
    """
    # Define text file write parameters
    path = FILES_DIR
    filename = "output_top_view_count.txt"
    out_file_path = f"{path}/{filename}"
    mode = "w"
    encoding = "utf-8"
    with open(file=out_file_path, mode=mode, encoding=encoding) as file:
        post_id = None
        view_count = None
        for dictionary in key_value_list:
            # Finding elementes.
            post_id = dictionary["post_id"]
            view_count = dictionary["view_count"]
            file.write(
                f"post_id:\t{post_id}\tview_count:\t{view_count}\n")
        file.close()


"""Top 10 words by tag"""


def word_by_tag_mapper() -> list:
    """This function reads a .xml file, searches for "post tag", and "post word" and counts 
    it to append these values in a dictionary within a list of dictionaries.

    Returns:
        list: List of dictionaries sort descending by "post_tag" and "post_body_word" with format: 
        {"post_tag": post_tag, "post_body_word": post_body_word, "count": count}
    """
    mytree = ET.parse(f"{DATASETS_DIR}/posts.xml")
    # instance "of" the root tree.
    myroot = mytree.getroot()
    top_limit01 = len(myroot)
    KEY_VALUE_LIST = []
    post_tag = None
    post_body_word = None
    count = None
    for row in range(0, top_limit01):
        # Finding elementes.
        try:
            # Clean XML tags from text on "Body" attribute
            text = myroot[row].attrib["Body"]
            clean_body_text = LH.fromstring(text)
            clean_body_text = clean_body_text.text_content()
            clean_body_text = re.sub(r'\n', ' ', clean_body_text)
            clean_body_text = clean_body_text.split()
            # Clean XML tags from text on "Tags" attribute.
            clean_tag_text = re.sub(r'\W+', ' ', myroot[row].attrib["Tags"])
            clean_tag_text = clean_tag_text.split()
        except KeyError:
            continue
        except LH.etree.ParserError:
            continue
        # Append finded elements to dictionary within list of dictionaries.
        for tag in clean_tag_text:
            post_tag = tag
            for word in clean_body_text:
                post_body_word = word
                count = 1
                KEY_VALUE_LIST.append(
                    {"post_tag": post_tag,
                     "post_body_word": post_body_word,
                     "count": count})  # ({"post_tag": post_tag, "post_body_word": post_body_word, "count":})

    # Sort list by "post_tag" and "count".
    KEY_VALUE_LIST = sorted(
        KEY_VALUE_LIST, key=operator.itemgetter("post_tag", "post_body_word"), reverse=False)

    return KEY_VALUE_LIST


def word_by_tag_reducer(key_value_list: list) -> list:
    """This function count de number of words by tag and append these values 
    in a dictionary within a list of dictionaries..

    Args:
        key_value_list (list): List of dictionaries sort descending by "post_tag" and "post_body_word" with format: 
        {"post_tag": post_tag, "post_body_word": post_body_word, "count": count}

    Returns:
        list: List of dictionaries sort descending by "post_tag" and "count" with 
        format: {"post_tag": post_tag, "post_body_word": post_body_word, "count": count}
    """
    WORD_BY_CATEGORY = []
    current_word = None
    current_tag = None
    word_count = None
    # Finding elementes.
    for dictionary in key_value_list:
        tag = dictionary["post_tag"]
        word = dictionary["post_body_word"]
        count = dictionary["count"]

        if current_word == word:
            word_count += count
        else:
            if current_word:
                # Append finded elements to dictionary within list of dictionaries.
                WORD_BY_CATEGORY.append(
                    {"post_tag": current_tag,
                     "post_body_word": current_word,
                     "count": word_count})

            # Update values.
            current_word = word
            current_tag = tag
            word_count = count

    # Validate last word iteration.
    if current_word == word:
        # Append finded elements to dictionary within list of dictionaries.
        WORD_BY_CATEGORY.append(
            {"post_tag": current_tag,
             "post_body_word": current_word,
             "count": word_count})
    # Sort list by "post_tag" and "count".
    WORD_BY_CATEGORY = sorted(
        WORD_BY_CATEGORY, key=operator.itemgetter("post_tag", "count"), reverse=False)
    return WORD_BY_CATEGORY


def top_word_by_tag_calculator(key_value_list: list) -> object:
    """This function iter through a list of dictionaries and calculate
    the top 10 most repeated words by tag.

    Args:
        key_value_list (list): List of dictionaries sort descending by "post_tag" and "count" with 
        format: {"post_tag": post_tag, "post_body_word": post_body_word, "count": count}

    Returns:
        object: Text file with top 10 most repeated words by tag.
    """
    word_by_tag = key_value_list
    top_limit = len(word_by_tag)
    current_tag = None
    aux_dict = None
    post_tag = None
    post_body_word = None
    count = None
    top_word_by_category = []

    for i in range(0, top_limit):
        # Finding elementes.
        dictionary01 = word_by_tag[i]
        next_tag = dictionary01["post_tag"]

        # Validate tag iteration.
        if current_tag == next_tag:
            pass
        else:
            if current_tag:
                # Start countdown since current list index (dictionary) to append the
                # top 10 most repeated words for the set tag.
                counter = 1
                while counter <= 10:
                    to_dict_indx = (i - counter)
                    aux_dict = word_by_tag[to_dict_indx]
                    top_word_by_category.append(aux_dict)
                    counter += 1

            current_tag = next_tag
    # Validate last tag iteration.
    if current_tag == next_tag:
        counter = 1
        # Start countdown since current list index (dictionary) to append the
        # top 10 most repeated words for the set tag.
        while counter <= 10:
            to_dict_indx = (i - counter)
            aux_dict = word_by_tag[to_dict_indx]
            top_word_by_category.append(aux_dict)
            counter += 1

    # Define text file write parameters
    path = FILES_DIR
    filename = "output_top_words_by_tag.txt"
    out_file_path = f"{path}/{filename}"
    mode = "w"
    encoding = "utf-8"

    with open(file=out_file_path, mode=mode, encoding=encoding) as file:
        for dictionary in top_word_by_category:
            post_tag = dictionary["post_tag"]
            post_body_word = dictionary["post_body_word"]
            count = dictionary["count"]
            file.write(
                f"post_tag:\t{post_tag}\tpost_body_word:\t{post_body_word}\tcount:\t{count}\n")
        file.close()


"""Top 10 most viwed post"""
