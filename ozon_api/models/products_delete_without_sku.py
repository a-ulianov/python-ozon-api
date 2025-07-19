from typing import List, Optional

from pydantic import BaseModel, Field


class ProductDeleteWithoutSkuRequest(BaseModel):
    """Запрос на удаление товара без SKU."""

    offer_id: str = Field(
        ..., description="Идентификатор товара в системе продавца — offer_id."
    )


class ProductDeleteWithoutSkuStatus(BaseModel):
    """Статус удаления товара."""

    error: Optional[str] = Field(..., description="Описание ошибки.")
    is_deleted: bool = Field(..., description="Статус удаления товара.")
    offer_id: str = Field(
        ..., description="Идентификатор товара в системе продавца — offer_id."
    )


class ProductDeleteWithoutSkuResponse(BaseModel):
    """Ответ на запрос удаления товара без SKU."""

    status: List[ProductDeleteWithoutSkuStatus]
