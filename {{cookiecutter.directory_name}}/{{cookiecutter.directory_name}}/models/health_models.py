"""Data models for health routes
"""
from pydantic import BaseModel


class WelcomeAPIModel(BaseModel):
    message: str


class HealthModel(BaseModel):
    status: str
