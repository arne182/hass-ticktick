"""ticktick api client"""
import datetime
import json
from typing import Dict

from ticktick import OAuth2, TickTickClient

from .const import ADD_TASK_URL, AUTH_URL, PROJECT_URL, TICKTICK_HOST



class TickTick:
    """TickTick API Client using ticktick-py"""

    def __init__(self, client_id, client_secret):
        self.auth_client = OAuth2(client_id=client_id, client_secret=client_secret, redirect_uri="http://127.0.0.1:8080")
        self.client = None

    def login(self, username, password):
        """Log into TickTick using ticktick-py. ValueError is thrown when credentials are incorrect"""
        self.client = TickTickClient(username, password, self.auth_client)

    
    def fetch_tasks_from_project(self, project_id):
        """Fetch tasks from a specific TickTick project using ticktick-py."""
        # Filtering tasks based on the given project_id
        tasks = [task for task in self.client.state["tasks"] if task['projectId'] == project_id]
        return tasks
