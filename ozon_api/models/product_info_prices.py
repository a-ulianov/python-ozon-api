from enum import Enum
from typing import Optional, List

from pydantic import BaseModel, Field

class Visibility(str, Enum):
    """Фильтр по видимости товара."""
    ALL = "ALL"
    """все товары."""
    VISIBLE = "VISIBLE"
    """товары, которые видны покупателям."""
    INVISIBLE = "INVISIBLE"
    """товары, которые не видны покупателям."""
    EMPTY_STOCK = "EMPTY_STOCK"
    """товары, у которых не указано наличие."""
    NOT_MODERATED = "NOT_MODERATED"
    """товары, которые не прошли модерацию."""
    MODERATED = "MODERATED"
    """товары, которые прошли модерацию."""
    DISABLED = "DISABLED"
    """товары, которые видны покупателям, но недоступны к покупке."""
    STATE_FAILED = "STATE_FAILED"
    """товары, создание которых завершилось ошибкой."""
    READY_TO_SUPPLY = "READY_TO_SUPPLY"
    """товары, готовые к поставке."""
    VALIDATION_STATE_PENDING = "VALIDATION_STATE_PENDING"
    """товары, которые проходят проверку валидатором на премодерации."""
    VALIDATION_STATE_FAIL = "VALIDATION_STATE_FAIL"
    """товары, которые не прошли проверку валидатором на премодерации."""
    VALIDATION_STATE_SUCCESS = "VALIDATION_STATE_SUCCESS"
    """товары, которые прошли проверку валидатором на премодерации."""
    TO_SUPPLY = "TO_SUPPLY"
    """товары, готовые к продаже."""
    IN_SALE = "IN_SALE"
    """товары в продаже."""
    REMOVED_FROM_SALE = "REMOVED_FROM_SALE"
    """товары, скрытые от покупателей."""
    OVERPRICED = "OVERPRICED"
    """товары с завышенной ценой."""
    CRITICALLY_OVERPRICED = "CRITICALLY_OVERPRICED"
    """товары со слишком завышенной ценой."""
    EMPTY_BARCODE = "EMPTY_BARCODE"
    """товары без штрихкода."""
    BARCODE_EXISTS = "BARCODE_EXISTS"
    """товары со штрихкодом."""
    QUARANTINE = "QUARANTINE"
    """товары на карантине после изменения цены более чем на 50%."""
    ARCHIVED = "ARCHIVED"
    """товары в архиве."""
    OVERPRICED_WITH_STOCK = "OVERPRICED_WITH_STOCK"
    """товары в продаже со стоимостью выше, чем у конкурентов."""
    PARTIAL_APPROVED = "PARTIAL_APPROVED"
    """товары в продаже с пустым или неполным описанием."""


class ProductInfoPricesRequestFilter(BaseModel):
    """Фильтр по товарам для тела запроса."""
    offer_id: Optional[List[str]] = Field(
        default_factory=list, description="Фильтр по параметру offer_id. Можно передавать до 1000 значений."
    )
    product_id: Optional[List[str]] = Field(
        default_factory=list, description="Фильтр по параметру product_id. Можно передавать до 1000 значений."
    )
    visibility: Optional[Visibility] = Field(
        Visibility.ALL, description="Фильтр по видимости товара."
    )


class ProductInfoPricesRequest(BaseModel):
    """Формирует модель, описывающую тело запроса."""
    cursor: str = Field(
        str(), description="Указатель для выборки следующих данных."
    )
    filter: ProductInfoPricesRequestFilter = Field(
        ProductInfoPricesRequestFilter(), description="Фильтр по товарам."
    )
    limit: Optional[int] = Field(
        1000, description="Количество значений на странице. Максимум 1000.",
        ge=0, le=1000
    )


class ProductInfoPricesResponse(BaseModel):
    """Описывает схему ответа с информацией о цене товара."""
    cursor: str = Field(
        ..., description="Указатель для выборки следующих данных."
    )
    items: list = Field(
        ..., description="Массив данных о ценах."
    )
    total: int = Field(
        ..., description="Количество товаров в списке."
    )

