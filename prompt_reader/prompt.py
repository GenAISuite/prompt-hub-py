from functools import lru_cache
from db_config import DBConfig

class PromptReader:
    def __init__(self):
        self.db = DBConfig()

    @lru_cache(maxsize=100)
    def get_prompt_by_name(self, name):
        """
        Fetches the prompt by name from the PostgreSQL database.
        Uses LRU cache to cache up to 100 prompts.
        """
        try:
            prompt = self.db.run_query(name)
        except Exception as e:
            print(f"Error fetching prompt: {e}")
            raise
        return prompt

    def invalidate_cache(self):
        """Clears the cache."""
        self.get_prompt_by_name.cache_clear()

    def close(self):
        """Close the database connection."""
        self.db.close()
