# HF architecture dict:
arch_dict = {
    # https://huggingface.co/docs/transformers/model_doc/roberta#roberta
    "roberta": {
        "config_names": {
            "context_length": "max_position_embeddings",
            "vocab_size": "vocab_size",
            "width": "hidden_size",
            "heads": "num_attention_heads",
            "layers": "num_hidden_layers",
            "layer_attr": "layer",
            "token_embeddings_attr": "embeddings",
        },
        "pooler": "mean_pooler",
    },
    # https://huggingface.co/docs/transformers/model_doc/xlm-roberta#transformers.XLMRobertaConfig
    "xlm-roberta": {
        "config_names": {
            "context_length": "max_position_embeddings",
            "vocab_size": "vocab_size",
            "width": "hidden_size",
            "heads": "num_attention_heads",
            "layers": "num_hidden_layers",
            "layer_attr": "layer",
            "token_embeddings_attr": "embeddings",
        },
        "pooler": "mean_pooler",
    },
    # https://huggingface.co/docs/transformers/model_doc/mt5#mt5
    "mt5": {
        "config_names": {
            # unlimited seqlen
            # https://github.com/google-research/text-to-text-transfer-transformer/issues/273
            # https://github.com/huggingface/transformers/blob/v4.24.0/src/transformers/models/t5/modeling_t5.py#L374
            "context_length": "",
            "vocab_size": "vocab_size",
            "width": "d_model",
            "heads": "num_heads",
            "layers": "num_layers",
            "layer_attr": "block",
            "token_embeddings_attr": "embed_tokens",
        },
        "pooler": "mean_pooler",
    },
    # https://huggingface.co/docs/transformers/model_doc/bert
    "bert": {
        "config_names": {
            "context_length": "max_position_embeddings",
            "vocab_size": "vocab_size",
            "width": "hidden_size",
            "heads": "num_attention_heads",
            "layers": "num_hidden_layers",
        },
        "pooler": "cls_pooler",
    },
    # https://huggingface.co/docs/transformers/model_doc/m2m_100
    "m2m_100": {
        "config_names": {
            "context_length": "max_position_embeddings",
            "vocab_size": "vocab_size",
            "width": "d_model",
            "heads": "encoder_attention_heads",
            "layers": "encoder_layers",
        },
        "pooler": "cls_pooler",
    },
    "ESMplusplus": {
        "config_names": {
            "context_length": "max_position_embeddings",
            "vocab_size": "vocab_size",
            "width": "hidden_size",
            "heads": "num_attention_heads",
            "layers": "num_hidden_layers",
        },
        "pooler": "mean_pooler",
    },
    "qwen2": {
        "config_names": {
            "context_length": "max_position_embeddings",
            "vocab_size": "vocab_size",
            "width": "hidden_size",
            "heads": "num_attention_heads",
            "layers": "num_hidden_layers",
            "num_key_value_heads": "num_key_value_heads",
        },
        "pooler": "mean_pooler",
    },
}

#   "attention_dropout": 0.0,
#   "bos_token_id": 151643,
#   "eos_token_id": 151645,
#   "hidden_act": "silu",
#   "hidden_size": 896,
#   "initializer_range": 0.02,
#   "intermediate_size": 4864,
#   "max_position_embeddings": 32768,
#   "max_window_layers": 21,
#   "model_type": "qwen2",
#   "num_attention_heads": 14,
#   "num_hidden_layers": 24,
#   "num_key_value_heads": 2,
#   "rms_norm_eps": 1e-06,
#   "rope_theta": 1000000.0,
#   "sliding_window": 32768,
#   "tie_word_embeddings": true,
#   "torch_dtype": "bfloat16",
#   "transformers_version": "4.43.1",
#   "use_cache": true,
#   "use_sliding_window": false,
#   "vocab_size": 151936
