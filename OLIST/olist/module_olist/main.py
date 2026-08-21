from pathlib import Path
from dataset import load_dataset, create_dataset, save_dataset
from features import create_features


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
    # Salva o dataset final
    save_dataset(data,output_path,)

if __name__ == "__main__":
    main()