from ozon_api.methods.category import OzonCategoryAPI as Category
from ozon_api.methods.product_archive import OzonProductArchiveAPI as ProductArchive
from ozon_api.methods.product_barcode_add import (
    OzonProductBarcodeAddAPI as ProductBarcodeAdd,
)
from ozon_api.methods.product_barcode_generate import (
    OzonProductBarcodeGenerateAPI as ProductBarcodeGenerate,
)
from ozon_api.methods.product_import import OzonProductImportAPI as ProductImport
from ozon_api.methods.product_info_attributes import (
    OzonProductInfoAttributesAPI as ProductInfoAttributes,
)
from ozon_api.methods.product_info_list import OzonProductInfoListAPI as ProductInfoList
from ozon_api.methods.product_list import OzonProductListAPI as ProductList
from ozon_api.methods.product_pictures import OzonProductPicturesAPI as ProductPictures
from ozon_api.methods.product_pictures_info import (
    OzonProductPicturesInfoAPI as ProductPicturesInfo,
)
from ozon_api.methods.product_rating import OzonProductRatingAPI as ProductRating
from ozon_api.methods.product_related_sku import (
    OzonProductRelatedSkuAPI as ProductRelatedSku,
)
from ozon_api.methods.product_subscription import (
    OzonProductSubscriptionAPI as ProductSubscription,
)
from ozon_api.methods.product_update_offer_id import (
    OzonProductUpdateOfferIdAPI as ProductUpdateOfferId,
)

__all__ = [
    "ProductImport",
    "ProductInfoList",
    "ProductInfoAttributes",
    "ProductList",
    "ProductArchive",
    "ProductRating",
    "ProductSubscription",
    "ProductPicturesInfo",
    "ProductRelatedSku",
    "ProductUpdateOfferId",
    "ProductBarcodeGenerate",
    "ProductBarcodeAdd",
    "ProductPictures",
    "Category",
    "ProductsDeleteWithoutSku",
    "UploadDigitalCodesInfo",
]
