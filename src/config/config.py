import yaml
from pathlib import Path
from dotenv import load_dotenv
from src.utils.file_utils import resolve_env_vars

# .env 파일 로드
load_dotenv()

CONFIG_PATH = Path(__file__).resolve().parent / "config.yaml"

with open(CONFIG_PATH, "r", encoding="utf-8") as f:
     raw_config = yaml.safe_load(f)

CONFIG = resolve_env_vars(raw_config)




