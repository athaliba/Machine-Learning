from pathlib import Path
from module_olist.dataset import load_dataset, create_dataset, save_dataset
from sklearn.model_selection import train_test_split
from module_olist.features import create_features
from module_olist.modeling.train import train_models
from module_olist.modeling.evaluate import evaluate_models


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
    orders, items, customers = load_dataset(orders_path,items_path,customers_path,)
    # Cria o dataset
    data = create_dataset(orders,items,customers,)
    # Cria as features
    data = create_features(data)

    # Salva dataset intermediário
    save_dataset(data,output_path,)

    # Separação das variáveis
    X = data.drop(columns=["is_late"])
    y = data["is_late"]
    # Train/Test split
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42,stratify=y,)

    # Treina modelos
    models = train_models(X_train,y_train,)
    # Avalia modelos
    evaluate_models(models,X_test,y_test,)

if __name__ == "__main__":
    main()