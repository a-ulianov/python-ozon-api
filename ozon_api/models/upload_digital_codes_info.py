from pydantic import BaseModel, Field


class UploadDigitalCodesInfoResult(BaseModel):
    """Результат проверки статуса загрузки цифровых кодов"""

    status: str = Field(..., description="Статус загрузки: pending, imported, failed.")


class UploadDigitalCodesInfoResponse(BaseModel):
    """Ответ на запрос статуса загрузки цифровых кодов"""

    result: UploadDigitalCodesInfoResult


class UploadDigitalCodesInfoRequest(BaseModel):
    """Запрос статуса загрузки цифровых кодов"""

    task_id: int = Field(
        ..., description="Идентификатор задачи на загрузку кодов активации."
    )
