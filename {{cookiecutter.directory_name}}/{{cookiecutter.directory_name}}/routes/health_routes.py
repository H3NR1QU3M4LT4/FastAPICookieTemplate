""" Health routes module
"""
from fastapi import APIRouter, status, Depends
from {{cookiecutter.directory_name}}.models.health_models import WelcomeAPIModel, HealthModel
from {{cookiecutter.directory_name}}.auth import get_api_key


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
async def perform_health_check():
    """
    Health endpoint
    - **status**: status (string) healthy status
    """
    return HealthModel(status="Healthy")

@router.get("/health_secure", tags=["health"], summary="Check API health", response_description="API status",
            status_code=status.HTTP_200_OK, dependencies=[Depends(get_api_key)])
async def perform_health_check_secure():
    """
    Health endpoint
    - **status**: status (string) healthy status
    """
    return HealthModel(status="Healthy")
