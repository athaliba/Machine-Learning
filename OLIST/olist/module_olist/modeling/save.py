import json
import joblib

from pathlib import Path
from loguru import logger


def save_model(
    model,
    model_name,
    threshold,
    model_path: Path,
    metadata_path: Path,
):

    joblib.dump(
        model,
        model_path,
    )

    metadata = {
        "model_name": model_name,
        "threshold": threshold,
    }

    with open(
        metadata_path,
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(
            metadata,
            file,
            indent=4,
        )

    logger.success(
        f"Modelo salvo: {model_path}"
    )

    logger.success(
        f"Metadados salvos: {metadata_path}"
    )