from typing import Optional
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field, validator
from models.user_model import UserModel


class InvoicesOut(BaseModel):
    id                              :Optional[int]
    client_id                       :Optional[int]
    invoice_number                  :Optional[str]
    sequence_number                 :Optional[int]
    recurring                       :Optional[str]
    date                            :Optional[str]
    due_date                        :Optional[int]
    status_id                       :Optional[int]
    recurring_cycle_id              :Optional[int]
    sub_total                       :Optional[float]
    discount_type                   :Optional[str]
    discount                        :Optional[float]
    total                           :Optional[float]
    received_amount                 :Optional[float]
    due_amount                      :Optional[float]
    notes                           :Optional[str]
    terms                           :Optional[str]
    created_by                      :Optional[int]
    deleted_at                      :Optional[str]
    created_at                      :Optional[str]
    updated_at                      :Optional[str]


    class Config:
        orm_mode = True