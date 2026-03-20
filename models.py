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

    def get_formatted_time(self):
        """Custom behavior method to format the datetime."""
        return self.timestamp.strftime("%b %d, %Y - %I:%M %p")

    def update_details(self, new_name, new_category, new_description):
        """Custom behavior to handle editing a business."""
        self.name = new_name
        self.category = new_category
        self.description = new_description

class Directory:
    """Manages the collection of businesses using a Stack (LIFO)."""
    def __init__(self):
        self.business_stack = []

    def add_business(self, business):
        """Pushes a new business onto the stack."""
        self.business_stack.append(business)

    def get_recent_businesses(self):
        """Returns businesses in Last-In, First-Out (LIFO) order."""
        return list(reversed(self.business_stack))
