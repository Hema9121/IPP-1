from ipp.logger import logging
from ipp.exception import InsuranceException
import sys

def div():
    try:
        logging.info("division by zero error")
        a=5/0
        return a
    except Exception as e:
        raise InsuranceException(e,sys) from e

div()
