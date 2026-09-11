import pandas as pd
import shap
import matplotlib.pyplot as plt

from loguru import logger

from module_olist.config import (
    FIGURES_DIR,
    INTERIM_DATA_DIR,
    MODELS_DIR,
)

from module_olist.modeling.predict import load_model

from module_olist.modeling.interpret import (
    prepare_data_for_shap,
    create_explainer,
    calculate_shap_values,
)


def main():

    # Carrega dataset preparado
    data = pd.read_csv(
        INTERIM_DATA_DIR / "olist_dataset.csv"
    )


    # Seleciona features utilizadas no modelo
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


    # Carrega modelo treinado
    model, model_name, threshold = load_model(
        model_path=MODELS_DIR / "best_model.joblib",
        metadata_path=MODELS_DIR / "metadata.json",
    )


    logger.info(
        f"Modelo analisado: {model_name}"
    )


    # Seleciona amostra para explicação
    X_sample = X.sample(
        n=500,
        random_state=42,
    )


    # Prepara dados para SHAP
    X_shap = prepare_data_for_shap(
        model,
        X_sample,
    )


    # Cria explicador
    explainer = create_explainer(
        model
    )


    # Calcula valores SHAP
    shap_values = calculate_shap_values(
        explainer,
        X_shap,
    )


    # Gera gráfico
    plt.figure()

    shap.summary_plot(
        shap_values,
        X_shap,
        show=False,
    )


    # Salva imagem
    plt.savefig(
        FIGURES_DIR / "shap_summary.png",
        bbox_inches="tight",
    )

    plt.close()


    logger.success(
        "Gráfico SHAP gerado com sucesso."
    )


if __name__ == "__main__":
    main()