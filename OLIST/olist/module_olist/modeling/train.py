from sklearn.pipeline import Pipeline
from loguru import logger


def train_model(
    model: Pipeline,
    X_train,
    y_train,
):

    logger.info("Treinando modelo final...")

    model.fit(
        X_train,
        y_train,
    )

    logger.success("Modelo treinado com sucesso.")

    return model