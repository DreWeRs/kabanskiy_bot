import dataclasses
import os

from dotenv import load_dotenv


@dataclasses.dataclass
class BotConfig:
    api_token: str


def load_config() -> BotConfig | None:
    load_dotenv()
    api_token = os.environ.get('API_TOKEN')
    return BotConfig(api_token=api_token)
