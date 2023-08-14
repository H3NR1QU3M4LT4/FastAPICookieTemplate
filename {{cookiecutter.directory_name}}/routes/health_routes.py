""" Health routes module
"""
from fastapi import APIRouter, status
from {{cookiecutter.directory_name}}.models.health_models import WelcomeAPIModel, HealthModel


router = APIRouter()


@router.get("/", tags=["health"], summary="Root info", response_description="Message string")
async def root():
    """
    Root endpoint
    - **message**: message (string) welcome message
    """
    return WelcomeAPIModel(message="Welcome to the API!")


@router.get("/health", tags=["health"], summary="Check API health", response_description="API status",
            status_code=status.HTTP_200_OK)
async def perform_healthcheck():
    """
    Health endpoint
    - **status**: status (string) healthy status
    """
    return HealthModel(status="Healthy")
