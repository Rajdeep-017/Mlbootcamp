import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('app1.log'),
        logging.StreamHandler()
    ]
)
logger=logging.getLogger("arithmetic app")
def add(a,b):
    res=a+b
    logger.debug(f"adding {a}+{b}= {res}")
    return res

def sub(a,b):
    res=a-b
    logger.debug(f"adding {a}-{b}= {res}")
    return res

def mul(a,b):
    res=a*b
    logger.debug(f"adding {a}*{b}= {res}")
    return res
def div(a,b):
    try:
        res=a*b
        logger.debug(f"adding {a}/{b}= {res}")
        return res
    except ZeroDivisionError:
        logger.error("divi by zero")
        return None
    
add(10,132)
sub(11,33)
mul(5,7)
div(6,8)
