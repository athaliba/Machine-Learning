from module_olist.config import (
    INTERIM_DATA_DIR,
    MODELS_DIR,
)

from module_olist.modeling.predict import (
    load_model,
    predict,
)

from loguru import logger
import pandas as pd


def main():

    # Carrega o dataset preparado
    data = pd.read_csv(
        INTERIM_DATA_DIR / "olist_dataset.csv"
    )


    # Seleciona somente as features utilizadas no treinamento
    X = data[
        [
            "promised_days",
            "item_count",
            "seller_count",
            "total_price",
            "total_freight",
            "purchase_month",
            "purchase_weekday",
            "purchase_hour",
            "customer_state",
        ]
    ]


    # Seleciona algumas amostras para teste de inferência
    X_sample = X.sample(
        n=5,
        random_state=42,
    )


    # Carrega modelo treinado e metadados
    model, model_name, threshold = load_model(
        model_path=(
            MODELS_DIR /
            "best_model.joblib"
        ),
        metadata_path=(
            MODELS_DIR /
            "metadata.json"
        ),
    )


    # Realiza a previsão
    predictions = predict(
        model=model,
        X=X_sample,
        threshold=threshold,
    )


    logger.info(
        f"Amostras selecionadas:\n{X_sample}"
    )

    logger.success(
        f"Modelo utilizado: {model_name}\n"
        f"Predições realizadas:\n{predictions}"
    )


if __name__ == "__main__":
    main()