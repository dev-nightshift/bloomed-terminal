from typing import Dict, Any
from transformers import AutoConfig
from .settings import settings

_cached: Dict[str, Any] | None = None

def get_model_info() -> Dict[str, Any]:
    global _cached
    if _cached is not None:
        return _cached
    cfg = AutoConfig.from_pretrained(settings.model_dir, trust_remote_code=True)
    _cached = {
        "model_dir": settings.model_dir,
        "architectures": getattr(cfg, "architectures", None),
        "vocab_size": getattr(cfg, "vocab_size", None),
        "hidden_size": getattr(cfg, "hidden_size", None),
        "num_attention_heads": getattr(cfg, "num_attention_heads", None),
        "num_hidden_layers": getattr(cfg, "num_hidden_layers", None),
        "max_position_embeddings": getattr(cfg, "max_position_embeddings", None),
        "tie_word_embeddings": getattr(cfg, "tie_word_embeddings", None),
        "torch_dtype": str(getattr(cfg, "torch_dtype", None)),
    }
    return _cached
