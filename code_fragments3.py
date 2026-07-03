avg_latency = df["response_time_ms"].mean()
p95_latency = float(np.percentile(df["response_time_ms"], 95))
avg_tokens = df["tokens_generated"].mean()
error_rate = (df["_error_norm"] != "none").mean() * 100.0
avg_satisfaction = df["user_satisfaction"].mean()

## ------------------------------------------------------ ##
reproducible_model_config = {"llm_sha" : "LLM@abc123",
                            "adapters" : ["lora_med_safety_v2@e91f",
                                            "lora_math_v1@bb07"],
                            "input_sha" : "INPUT@p1e3",
                            "tokenizer_sha" : "TOK@t99",
                            "sampling" : {"temperature" : 0.2,
                                            "top_p" : 0.9},
                            "reward_model_sha" : "RM_EVAL@9af2",
                            "verifiers" : {"json_schema" : "v4.3",
                                            "span" : "v2.1",
                                            "unit_tests" : "v2.0"},
                            "tools" : {"search_api" : "3.2.1",
                                        "fixtures" : "search_v3.json",
                                        "repo_sha" : "GIT_SHA_CODEBASE_V3"}
                            }
