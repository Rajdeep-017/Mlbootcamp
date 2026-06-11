import logging
logging.basicConfig(
    level=logging.DEBUG,
    filename='app.log',
    filemode='w',
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
#configure the basic logging setting
logging.basicConfig(level=logging.DEBUG)
logging.debug('this is a debug meg')
logging.info('this is an info meg')
logging.warning("warning msg")
logging.error("this is error")
logging.critical('critical msg')