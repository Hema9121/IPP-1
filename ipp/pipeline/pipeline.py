#from collections import namedtuple
from datetime import datetime
#import uuid
from ipp.config.configuration import Configuartion
from ipp.logger import logging#,get_log_file_name
from ipp.exception import InsuranceException
#from threading import Thread
from typing import List

#from multiprocessing import Process
from ipp.entity.artifact_entity import DataIngestionArtifact#,ModelPusherArtifact, ModelEvaluationArtifact
#from ipp.entity.artifact_entity import DataValidationArtifact, DataTransformationArtifact, ModelTrainerArtifact
from ipp.entity.config_entity import DataIngestionConfig#, ModelEvaluationConfig
from ipp.components.data_ingestion import DataIngestion
"""from ipp.component.data_validation import DataValidation
from ipp.component.data_transformation import DataTransformation
from ipp.component.model_trainer import ModelTrainer
from ipp.component.model_evaluation import ModelEvaluation
from ipp.component.model_pusher import ModelPusher"""
import os, sys
import pandas as pd
#from ipp.constant import EXPERIMENT_DIR_NAME, EXPERIMENT_FILE_NAME

"""Experiment = namedtuple("Experiment", ["experiment_id", "initialization_timestamp", "artifact_time_stamp",
                                       "running_status", "start_time", "stop_time", "execution_time", "message",
                                       "experiment_file_path", "accuracy", "is_model_accepted"])"""

class Pipeline():
    """experiment: Experiment = Experiment(*([None] * 11))
    experiment_file_path = None"""
    
    def __init__(self, config: Configuartion ) -> None:
        try:
            """os.makedirs(config.training_pipeline_config.artifact_dir, exist_ok=True)
            Pipeline.experiment_file_path=os.path.join(config.training_pipeline_config.artifact_dir,EXPERIMENT_DIR_NAME, EXPERIMENT_FILE_NAME)
            super().__init__(daemon=False, name="pipeline")"""
            self.config = config
        except Exception as e:
            raise InsuranceException(e, sys) from e

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise InsuranceException(e, sys) from e
        
    def run_pipeline(self):
        try:
            """if Pipeline.experiment.running_status:
                logging.info("Pipeline is already running")
                return Pipeline.experiment
            # data ingestion
            logging.info("Pipeline starting.")

            experiment_id = str(uuid.uuid4())

            Pipeline.experiment = Experiment(experiment_id=experiment_id,
                                             initialization_timestamp=self.config.time_stamp,
                                             artifact_time_stamp=self.config.time_stamp,
                                             running_status=True,
                                             start_time=datetime.now(),
                                             stop_time=None,
                                             execution_time=None,
                                             experiment_file_path=Pipeline.experiment_file_path,
                                             is_model_accepted=None,
                                             message="Pipeline has been started.",
                                             accuracy=None,
                                             )
            logging.info(f"Pipeline experiment: {Pipeline.experiment}")

            self.save_experiment()"""

            data_ingestion_artifact = self.start_data_ingestion()
        except Exception as e:
            raise InsuranceException(e, sys) from e
    def run(self):
        try:
            self.run_pipeline()
        except Exception as e:
            raise e
