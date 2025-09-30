from ozon_api.base import OzonAPIBase
from ozon_api.models.product_info_prices import (
    ProductInfoPricesRequest, ProductInfoPricesResponse
)
from ozon_api.models.product_info_prices import ProductInfoPricesRequest


class OzonProductInfoPricesAPI(OzonAPIBase):
    async def product_info_prices(
        self: "OzonProductInfoPricesAPI", request: ProductInfoPricesRequest = ProductInfoPricesRequest()
    ) -> ProductInfoPricesResponse:
        """
        Метод для получения информации о ценах товаров по их идентификаторам.

        :param request: Данные для получения информации о товарах
        :return: Ответ с информацией о товарах
        """
        data = await self._request(
            method="post",
            api_version="v5",
            endpoint="product/info/prices",
            json=request.model_dump(),
        )
        return ProductInfoPricesResponse(**data)
