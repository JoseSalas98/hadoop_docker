# import necesary libraries
from fileinput import close
from os import write
import xml.etree.ElementTree as ET

# instance xml file
mytree = ET.parse("posts.xml")
# instance of the root tree
myroot = mytree.getroot()
# print(myroot)
# print(myroot.tag)
# print(myroot[0].tag)
# print(myroot[0].attrib)
# print(myroot[0].attrib["Id"])
# print(len(myroot))

# master mapper
# this script iter over xml file,
# search over the "match_list" (interests attributes (keys values)
# of rows (dictionary)) and return their content to solve ticket items
"""
count = 1
for n in myroot:
    count += 1
#   finding elementes
    for x in myroot[count].attrib:
        match_list = ["Id", "PostTypeId", "ParentID", "AcceptedAnswerId",
                     "CreationDate", "Score", "ViewCount", "Body"]
        id = None
        post_type_id = None
        parent_id = None
        accepte_answer_id = None
        creation_date = None
        score = None
        view_count = None
        body = None
        if x in match_list:
            if x == "Id":
                id = myroot[count].attrib[x]
                print(f"{x}: \t {myroot[count].attrib[x]}", 1)
                continue
            elif x == "PostTypeId":
                post_type_id = myroot[count].attrib[x]
                print(f"{x}: \t {myroot[count].attrib[x]}", 1)
                continue
            elif x == "ParentID":
                parent_id = myroot[count].attrib[x]
                print(f"{x}: \t {myroot[count].attrib[x]}", 1)
                continue
            elif x == "AcceptedAnswerId":
                accepte_answer_id = myroot[count].attrib[x]
                print(f"{x}: \t {myroot[count].attrib[x]}", 1)
                continue
            elif x == "CreationDate":
                creation_date = myroot[count].attrib[x]
                print(f"{x}: \t {myroot[count].attrib[x]}", 1)
                continue
            elif x == "Score":
                score = myroot[count].attrib[x]
                print(f"{x}: \t {myroot[count].attrib[x]}", 1)
                continue
            elif x == "ViewCount":
                view_count = myroot[count].attrib[x]
                print(f"{x}: \t {myroot[count].attrib[x]}", 1)
                continue
            elif x == "Body":
                body = myroot[count].attrib[x]
                print(f"{x}: \t {myroot[count].attrib[x]}", 1)
                continue
"""

# merge sort functions


def merge_sort(arr):
    if len(arr) <= 1:
        return

    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_lists(left, right, arr)


def merge_two_sorted_lists(a, b, arr):
    len_a = len(a)
    len_b = len(b)

    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1

    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1

    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1


# mapper
"""
with open("mapper_out.txt", "w") as file:
    count = 0
    for n in myroot:
        #   finding elementes
        for x in myroot[count].attrib:
            match_list = ["Id", "PostTypeId", "ParentID", "AcceptedAnswerId",
                         "CreationDate", "Score", "ViewCount", "Body"]
            if x in match_list:
                if x == "ViewCount":
                    file.write(f"{myroot[count].attrib[x]}: \t 1\n")
        count += 1
    # print(KEY_VALUE_LIST[0][0])
    file.close()
"""

# this script return view count and build pair: key value -
# count, to save on a child list, which append to main list
count = 0
KEY_VALUE_LIST = []
for n in myroot:
    #   finding elementes
    for x in myroot[count].attrib:
        key_value = []
        match_list = ["Id", "PostTypeId", "ParentID", "AcceptedAnswerId",
                      "CreationDate", "Score", "ViewCount", "Body"]
        if x in match_list:
            if x == "ViewCount":
                key_value.append(int(myroot[count].attrib[x]))
                key_value.append(1)
                KEY_VALUE_LIST.append(key_value)
    count += 1

# this script sort ascending the KEY_VALUE_LIST
merge_sort(KEY_VALUE_LIST)

# thi script write and txt file throught iteration of KEY_VALUE_LIST
with open("mapper_out.txt", "w") as file:
    count = 0
    for n in KEY_VALUE_LIST:
        file.write(
            f"ViewCount {KEY_VALUE_LIST[count][0]}:\t{KEY_VALUE_LIST[count][1]}\n")
        count += 1
    file.close()

# reducer
line = None
current_item = None
current_count = None

KEY_VALUE_LIST = []
with open("mapper_out.txt") as file:
    for line in file:
        #key_value = []
        line = line.strip()
        item, count = line.split(sep="\t")

        try:
            count = int(count)
        except ValueError:
            continue

        if current_item == item:
            current_count += count
        else:
            if current_item:
                # print("%s\t%s" % (current_item, current_count))
                KEY_VALUE_LIST.append([current_item, current_count])
                pass

            current_item = item
            current_count = count

if current_item == item:
    # print("%s\t%s" % (current_item, current_count))
    KEY_VALUE_LIST.append([current_item, current_count])
    pass

# print(KEY_VALUE_LIST)
top_viwe_post = KEY_VALUE_LIST[-10:]
# top_viwe_post = top_viwe_post[::-1]  # corte extendido
top_viwe_post.reverse()  # método reverse

# top view post calculator
top_limit01 = len(top_viwe_post)
top_limit02 = len(myroot)
for i in range(0, top_limit01):
    on_top_viwe = top_viwe_post[i][0]
    on_top_viwe = on_top_viwe.split(sep=" ")[1]
    on_top_viwe = int(on_top_viwe.replace(":", ""))
    for row in range(0, top_limit02):
        # finding elementes
        for view in myroot[row].attrib["ViewCount"]:
            view = int(myroot[row].attrib["ViewCount"])
            if view == on_top_viwe:
                post_id = myroot[row].attrib["Id"]
                print(f"El post {post_id} está en el top de más vistos")
                break

"""
top_limit = len(myroot)
for row in range(0, top_limit):
    print(row)
    # finding elementes
    #for view in myroot[row].attrib["ViewCount"]:
        #print(view)
"""
