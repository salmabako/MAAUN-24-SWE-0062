import uuid
from datetime import datetime

class Business:
    """Blueprint for a local business entity."""
    def __init__(self, name, category, description):
        self.id = uuid.uuid4().hex
        self.name = name
        self.category = category
        self.description = description
        self.timestamp = datetime.now()
