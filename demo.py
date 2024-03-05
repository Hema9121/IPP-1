from ipp.pipeline.pipeline import Pipeline
from ipp.exception import InsuranceException
from ipp.logger import logging
import sys,os
from ipp.config.configuration import Configuartion
#from ipp.entity.insurance_predictor import InsurancePredictor,InsuranceData

"""def main():
    try:
        insurance_data = InsuranceData(age=19,
                                   sex="female",
                                   bmi=27.9,
                                   children=0,
                                   smoker="yes",
                                   region="southwest",)
        insurance_df = insurance_data.get_insurance_input_data_frame()
        pred=InsurancePredictor(model_dir="saved_models")
        expenses = pred.predict(X=insurance_df)
        print(expenses)
        return expenses
    except Exception as e:
        raise InsuranceException(e,sys) from e"""

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