from fastapi import FastAPI
from pydantic import BaseModel, SecretStr

app = FastAPI()

class SecretRequest(BaseModel):
    api_key: SecretStr

@app.post("/validate")
async def validate_key(request: SecretRequest):
    return {"valid": True, "key_last4": str(request.api_key.get_secret_value())[-4:]}
