from app import logging
def add(a,b):
    logging.debug("the addition operation")
    return a+b
logging.debug("the addition called")
add(3,6)
