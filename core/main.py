import modules.map_reduce_function as mp_funct
from threading import Thread

"""Top 10 most viwed post"""


def top_10_most_viwed_post():
    post_view_count_list = mp_funct.top_view_mapper()
    mp_funct.top_view_calculator(key_value_list=post_view_count_list)


"""Top 10 words by tag"""


def top_10_words_by_tag():
    word_by_tag = mp_funct.word_by_tag_mapper()
    word_by_tag = mp_funct.word_by_tag_reducer(key_value_list=word_by_tag)
    top_word_by_tag = mp_funct.top_word_by_tag_calculator(
        key_value_list=word_by_tag)


"""Response Time"""


def response_time():
    key_value_list = mp_funct.response_time_mapper()
    response_time_mean_value = mp_funct.response_time_mean_calculator(
        key_value_list=key_value_list)
    print(
        f"El tiempo promedio de respuesta para los posts es de {response_time_mean_value} segundos")


"""Main Program"""
if __name__ == "__main__":
    threads = []
    target_list = [top_10_most_viwed_post, top_10_words_by_tag, response_time]

    # Create threads and asign a function for each thread
    for function in range(target_list):
        thread = Thread(target=function)
        threads.append(thread)

    # Start all threads
    for thread in threads:
        thread.start()

    # Wait for all threads to finish
    # Block the main thread until these threads are finished
    for thread in threads:
        thread.join()
