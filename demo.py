from ipp.pipeline.pipeline import Pipeline
from ipp.exception import InsuranceException
from ipp.logger import logging
import sys,os
from ipp.config.configuration import Configuartion



def main():
    try:
        config_path = os.path.join("config","config.yaml")
        logging.info("testing")
        pipeline=Pipeline(Configuartion())
        pipeline.run_pipeline()
        #pipeline.start()
        logging.info("testing completed")
    except Exception as e:
        raise InsuranceException(e,sys) from e
    
if __name__=="__main__":
    main()