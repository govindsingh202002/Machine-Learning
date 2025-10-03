import logging
logger1=logging.getLogger("Module1")
logger1.setLevel(logging.DEBUG)
logger2=logging.getLogger("Module2")
logger2.setLevel(logging.DEBUG)

logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s-%(name)s_%(levelname)s-%(message)s",
        datefmt="%H:%M:%S %y-%m-%d"

                        )
logger1.debug("This is a debug message")
logger2.info("This is an info message")
logger1.warning("This is a warning message")
logger2.error("This is an error message")
logger1.critical("This is a critical error")
