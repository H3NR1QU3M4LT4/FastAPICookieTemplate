""" This module contains the authentication logic for the API.
"""
from dotenv import load_dotenv
from fastapi.security.api_key import APIKeyHeader
from fastapi import Security, HTTPException
import os
from starlette.status import HTTP_403_FORBIDDEN


load_dotenv()
api_key = os.getenv("AccessToken")


access_token = APIKeyHeader(name="AccessToken", auto_error=False)


async def get_api_key(api_key_header: str = Security(access_token)):
    if api_key_header == api_key:
        return api_key_header
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate API KEY"
        )
