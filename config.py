# config.py
import config_default,config_override
from Pandas import merge

configs = config_default.configs
try:
    configs = merge(configs,config_override.configs)
except ImportError:
    pass