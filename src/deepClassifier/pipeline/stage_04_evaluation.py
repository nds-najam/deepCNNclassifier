from deepClassifier.config import ConfigurationManager
from deepClassifier.components import Evaluation
from deepClassifier import logger


STAGE_NAME = "Evaluation Stage"

def main():
    config = ConfigurationManager()
    val_config = config.get_validation_config()
    evaluation = Evaluation(val_config)
    evaluation.evaluation()
    evaluation.save_score()
    evaluation.log_info_mlflow()

if __name__ == '__main__':
    try:
        logger.info(f"*************")
        logger.info(f"\n\n>>>>>> stage {STAGE_NAME} started <<<<<<")
        main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed \n\n<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e