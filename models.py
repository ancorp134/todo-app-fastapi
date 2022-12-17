from pydantic import BaseModel

class todo(BaseModel):
    task : str
    desc : str