import pandas as pd
import shap

from scipy import sparse


def prepare_data_for_shap(
    pipeline,
    X: pd.DataFrame,
):
    """
    Prepara os dados para o SHAP aplicando
    o mesmo pré-processamento utilizado no treinamento.
    """

    preprocessor = pipeline.named_steps["preprocessor"]

    X_transformed = preprocessor.transform(X)

    # Converte matriz esparsa para formato comum
    if sparse.issparse(X_transformed):
        X_transformed = X_transformed.toarray()

    # Recupera nomes das features após OneHotEncoder
    feature_names = (
        preprocessor
        .get_feature_names_out()
    )

    X_transformed = pd.DataFrame(
        X_transformed,
        columns=feature_names,
        index=X.index,
    )

    return X_transformed



def create_explainer(
    pipeline,
):
    """
    Cria o explicador SHAP para modelos baseados
    em árvores (LightGBM, XGBoost e Gradient Boosting).
    """

    model = pipeline.named_steps["model"]

    explainer = shap.TreeExplainer(
        model
    )

    return explainer



def calculate_shap_values(
    explainer,
    X_transformed: pd.DataFrame,
):
    """
    Calcula os valores SHAP das amostras.
    """

    shap_values = explainer.shap_values(
        X_transformed
    )

    return shap_values