import os
import operator
import xml.etree.ElementTree as ET
from pathlib import Path

# Paths
MAIN_DIR = Path(f"{os.path.dirname(os.path.realpath(__file__))}").parent.parent
CORE_DIR = Path(f"{MAIN_DIR}/core")
FILES_DIR = Path(f"{MAIN_DIR}/files")
DATASETS_DIR = Path(f"{MAIN_DIR}/datasets")
# print(f"{MAIN_DIR}\n{CORE_DIR}\n{FILES_DIR}\n{DATASETS_DIR}")


def top_view_mapper() -> list:
    """This function reads a .xml file, searches for "post id" and "post view count" and 
    appends these values in a dictionary within a list of dictionaries.

    Returns:
        list: List of dictionaries with format {"post_id": post_id, "view_count": view_count} 
    """
    mytree = ET.parse(f"{DATASETS_DIR}/posts.xml")
    # Instance of the root tree
    myroot = mytree.getroot()
    top_limit01 = len(myroot)
    post_id = None
    view_count = None
    KEY_VALUE_LIST = []
    for row in range(0, top_limit01):
        # Finding elementes
        try:
            post_id = int(myroot[row].attrib["Id"])
            view_count = int(myroot[row].attrib["ViewCount"])
        except ValueError:
            continue
        KEY_VALUE_LIST.append(
            {"post_id": post_id,
             "view_count": view_count}
        )

    KEY_VALUE_LIST = sorted(
        KEY_VALUE_LIST, key=operator.itemgetter("view_count"), reverse=True)

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
    path = FILES_DIR
    filename = "output_top_view_count.txt"
    out_file_path = f"{path}/{filename}"
    mode = "w"
    encoding = "utf-8"
    with open(file=out_file_path, mode=mode, encoding=encoding) as file:
        post_id = None
        view_count = None
        for dictionary in key_value_list:
            # Finding elementes
            post_id = dictionary["post_id"]
            view_count = dictionary["view_count"]
            file.write(
                f"post_id:\t{post_id}\tview_count:\t{view_count}\n")
        file.close()
