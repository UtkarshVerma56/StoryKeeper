from pydantic import BaseModel


class Memory(BaseModel):

    text: str

    category: str

    importance: int = 1