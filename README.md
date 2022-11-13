# deep CNN Classifier Project

## Workflow
1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration Manager in src config
6. Update the components
7. Update the pipeline
8. Test run pipeline stage
9. run tox for testing your package
10. run "dvc repro" for running all the stages in pipeline

![img](https://raw.githubusercontent.com/c17hawke/FSDS_NOV_deepCNNClassifier/main/docs/images/Data%20Ingestion%402x%20(1).png)

### on DAGSHUB
STEP 1: Set the env variable | Get it from dagshub -> remote tab -> mlflow tab

MLFLOW_TRACKING_URI=https://dagshub.com/c17hawke/FSDS_NOV_deepCNNClassifier.mlflow \
MLFLOW_TRACKING_USERNAME=c17hawke \
MLFLOW_TRACKING_PASSWORD=<> \

STEP 2: install mlflow

STEP 3: Set remote URI

STEP 4: Use context manager of mlflow to start run and then log metrics, params and model


## Sample data for testing-
https://raw.githubusercontent.com/c17hawke/raw_data/main/sample_data.zip

## docker
FROM python:3.8-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["streamlit","app.py"]

# Build docker image (docker should have installed on computer)
docker build -t pred_service
docker run -p 3000:3000 pred_service (normal mode)
docker run -dp 3000:3000 pred_service (detached mode)
docker run -i -p 3000:3000 pred_service (interactive mode)