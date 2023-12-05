from loguru import logger

from data_juicer.config import init_configs
from data_juicer.core import Executor

import sys
sys.path.append('.')


@logger.catch
def main():
    cfg = init_configs()
    executor = Executor(cfg)
    executor.run()


if __name__ == '__main__':
    main()
