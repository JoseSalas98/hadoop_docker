import modules.map_reduce_function as mp_funct

"""Top 10 most viwed post"""
post_view_count_list = mp_funct.top_view_mapper()
mp_funct.top_view_calculator(key_value_list=post_view_count_list)

"""Top 10 words by tag"""
word_by_tag = mp_funct.word_by_tag_mapper()
word_by_tag = mp_funct.word_by_tag_reducer(key_value_list=word_by_tag)
top_word_by_tag = mp_funct.top_word_by_tag_calculator(
    key_value_list=word_by_tag)

"""Response Time"""
key_value_list = mp_funct.response_time_mapper()
response_time_mean_value = mp_funct.response_time_mean_calculator(
    key_value_list=key_value_list)
print(
    f"El tiempo promedio de respuesta para los posts es de {response_time_mean_value} segundos")
