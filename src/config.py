HF_TOKEN = ""

# SAE checkpoint paths — set before running probe_features.py
LLAMA_AE_PATH = "./checkpoints/autoencoder.pt"
OLMO_AE_PATH = ""  # path or HF repo id for your OLMo-7B SAE, e.g. "./checkpoints/olmo_autoencoder.pt"

# Random model control experiment
# Architecture whose config is used to build the randomly initialized model
RANDOM_MODEL_BASE = "meta-llama/Meta-Llama-3-8B"
RANDOM_SAE_ACTIVATION_DIM = 4096   # must match RANDOM_MODEL_BASE hidden size
RANDOM_SAE_DICT_SIZE = 32768       # SAE expansion factor (8x default)
