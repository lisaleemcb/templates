# minimum working example for logging info
# this just parses through some integers and
# makes simple logs files
#
import logging

def setup_logger(logger_name, log_file, level=logging.INFO):
    handler = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger = logging.getLogger(logger_name)
    logger.setLevel(level)
    logger.addHandler(handler)

    # Clear existing handlers to avoid duplicate logs
    if logger.hasHandlers():
        logger.handlers.clear()

    logger.addHandler(handler)

    return logger

for i in range(5):
    logger_name = f'logger_{i}'
    log_file = f'file{i}.log'
    logger = setup_logger(logger_name, log_file)

    logger.info(f'Now on file {i}')

    if i >= 3:
        logger.warning('Big number!')

print('done!')
