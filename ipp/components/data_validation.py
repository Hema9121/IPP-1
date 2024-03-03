from ipp.logger import logging
from ipp.exception import InsuranceException
from ipp.constant import *
from ipp.entity.config_entity import DataValidationConfig
from ipp.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact
import os,sys
import pandas  as pd
import json
from ipp.config.configuration import Configuartion

class DataValidation:
    

    def __init__(self, data_validation_config:DataValidationConfig,
        data_ingestion_artifact:DataIngestionArtifact):
        try:
            logging.info(f"{'>>'*30}Data Valdaition log started.{'<<'*30} \n\n")
            self.data_validation_config = data_validation_config
            self.data_ingestion_artifact = data_ingestion_artifact
        except Exception as e:
            raise InsuranceException(e,sys) from e


    def get_train_and_test_df(self):
        try:
            train_df = pd.read_csv(self.data_ingestion_artifact.train_file_path)
            test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)
            return train_df,test_df
        except Exception as e:
            raise InsuranceException(e,sys) from e


    def is_train_test_file_exists(self)->bool:
        try:
            logging.info("Checking if training and test file is available")
            is_train_file_exist = False
            is_test_file_exist = False

            train_file_path = self.data_ingestion_artifact.train_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path

            is_train_file_exist = os.path.exists(train_file_path)
            is_test_file_exist = os.path.exists(test_file_path)

            is_available =  is_train_file_exist and is_test_file_exist

            logging.info(f"Is train and test file exists?-> {is_available}")
            
            if not is_available:
                training_file = self.data_ingestion_artifact.train_file_path
                testing_file = self.data_ingestion_artifact.test_file_path
                message=f"Training file: {training_file} or Testing file: {testing_file}" \
                    "is not present"
                raise Exception(message)

            return is_available
        except Exception as e:
            raise InsuranceException(e,sys) from e

    
    def validate_dataset_schema(self)->bool:
        try:
            validation_status = False
            
            #Assigment validate training and testing dataset using schema file
            #1. Number of Column
            #2. Check the value of region
            # acceptable values     
            # southeast
            # southwest
            # northeast
            # northwest
            #3. Check column names

            validation_status = True
            return validation_status 
        except Exception as e:
            raise InsuranceException(e,sys) from e
        
    def initiate_data_validation(self)->DataValidationArtifact:
        try:
            self.is_train_test_file_exists()
            self.validate_dataset_schema()

            data_validation_artifact=DataValidationArtifact(schema_file_path=self.data_validation_config.schema_file_path,
                                                            report_file_path=None,
                                                            report_page_file_path=None,
                                                            is_validated=True,message=f"data validation performed successfully!")
            logging.info(f"data validation artifact : {data_validation_artifact}")
            
            return data_validation_artifact

        except Exception as e:
            raise InsuranceException(e,sys) from e
    
    def __del__(self):
        logging.info(f"{'**'*20}data validation ended !{'**'*20}")