from pathlib import Path

from module_olist.dataset import load_dataset, create_dataset, save_dataset
from module_olist.features import create_features
from module_olist.modeling.split import split_data
from module_olist.modeling.cross_validation import cross_validate_models
from module_olist.modeling.pipeline import (
    create_gradient_boosting_pipeline,
    create_xgboost_pipeline,
    create_lightgbm_pipeline,
)
from module_olist.modeling.evaluate import evaluate_model


def main():
    # Diretório raiz do projeto OLIST
    base_dir = Path(__file__).resolve().parent.parent

    # Arquivos de entrada
    orders_path = base_dir / "data" / "raw" / "olist_orders_dataset.csv"
    items_path = base_dir / "data" / "raw" / "olist_order_items_dataset.csv"
    customers_path = base_dir / "data" / "raw" / "olist_customers_dataset.csv"

    # Arquivo de saída
    output_path = base_dir / "data" / "interim" / "olist_dataset.csv"

    # Carrega os dados
    orders, items, customers = load_dataset(
        orders_path, items_path, customers_path
    )

    # Cria o dataset
    data = create_dataset(orders, items, customers)

    # Cria as features
    data = create_features(data)

    # Salva dataset intermediário
    save_dataset(data, output_path)

    # Separa treino e teste
    X_train, X_test, y_train, y_test = split_data(data)

    # Cross Validation
    best_model_name, best_threshold = cross_validate_models(
        X_train, y_train
    )

    # Pipelines
    pipelines = {
        "Gradient Boosting": create_gradient_boosting_pipeline(),
        "XGBoost": create_xgboost_pipeline(),
        "LightGBM": create_lightgbm_pipeline(),
    }

    # Seleciona o melhor modelo
    best_model = pipelines[best_model_name]

    # Treina o melhor modelo com todo o conjunto de treino
    best_model.fit(X_train, y_train)

    # Avaliação final no conjunto de teste
    evaluate_model(
        best_model,
        X_test,
        y_test,
        best_threshold,
    )


if __name__ == "__main__":
    main()