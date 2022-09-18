from modules.map_reduce_function import top_view_mapper, top_view_calculator


post_view_count_list = top_view_mapper()

top_view_calculator(key_value_list=post_view_count_list)
