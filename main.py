import asyncio
import os

from dotenv import load_dotenv

from ozon_api import OzonAPI
from ozon_api.models import ProductInfoListRequest, ProductListRequest

async def main():
    load_dotenv()

    api = OzonAPI(
        client_id=os.environ['CLIENT_ID'],
        api_key=os.environ['API_KEY']
    )

    product_list = await api.product_list(
        request=ProductListRequest(
            filter={}
        )
    )

    for item in product_list.result.items:
        product_info = await api.product_info_list(
            request=ProductInfoListRequest(
                product_id=[item["product_id"], ]
            )
        )

        print(product_info)


if __name__ == "__main__":
    asyncio.run(main())