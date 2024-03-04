from ipp.pipeline.pipeline import Pipeline
from ipp.exception import InsuranceException
from ipp.logger import logging
import sys,os
from ipp.config.configuration import Configuartion

def main():
    try:
        config_path = os.path.join("config","config.yaml")
        pipeline = Pipeline(Configuartion(config_file_path=config_path))
        pipeline.run_pipeline()
        #pipeline.start()
        logging.info("main function execution completed.")

    except Exception as e:
        logging.error(f"{e}")
        print(e)



if __name__=="__main__":
    main()