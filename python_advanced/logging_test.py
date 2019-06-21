import logging

# create logger
name = 'test'
logger = logging.getLogger(name)
logger.setLevel(logging.DEBUG)  # ***

# create handler
filename = 'logging.log'
file_handler = logging.FileHandler(filename)
file_handler.setLevel(logging.WARNING)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)

# create formatter
fmt = "%(asctime)-15s %(levelname)s %(filename)s %(lineno)d %(process)d %(message)s"
datefmt = "%a %d %b %Y %H:%M:%S"
formatter = logging.Formatter(fmt, datefmt)

# add formatter to handler
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

# add handler to logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

logger.debug('debug...')
logger.info('info...')
logger.warning('warning...')
logger.error('error...')
logger.critical('critical...')
