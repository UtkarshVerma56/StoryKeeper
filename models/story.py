from pydantic import BaseModel


class StoryRequest(BaseModel):

    chapter: str