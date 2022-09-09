import logging
from logging import config
from os import path

log_file_path = path.join(path.dirname(
    path.abspath(__file__)), "log_file_config.conf")

config.fileConfig(log_file_path)


def addition(a, b):
    logging.debug("Inside Addition Function")
    if isinstance(a, str) and a.isdigit():
        logging.warning(
            "Warning : Parameter A is passed as String. Future versions won't support it.")

    if isinstance(b, str) and b.isdigit():
        logging.warning(
            "Warning : Parameter B is passed as String. Future versions won't support it.")

    try:
        result = float(a) + float(b)
        logging.info("Addition Function Completed Successfully")
        return result
    except Exception as e:
        logging.error("Error Type : {}, Error Message : {}".format(
            type(e).__name__, e))
        return None


if __name__ == "__main__":
    #logging.info("Current Log Level : {}\n".format(logging.getLevel()))
    a = 10
    b = 20
    result = addition(a, b)
    logging.info("Addition of {} & {} is : {}\n".format(a, b, result))

    a = "20"
    b = 20
    result = addition(a, b)
    logging.info("Addition of {} & {} is : {}\n".format(a, b, 20, result))

    a = "A"
    b = 20
    result = addition(a, b)
    logging.info("Addition of {} & {} is : {}".format(a, b, result))
