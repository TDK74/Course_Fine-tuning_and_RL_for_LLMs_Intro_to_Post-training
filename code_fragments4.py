from transformers import AutoModelForSeq2SeqLM
from peft import LoraModel, LoraConfig


## ------------------------------------------------------ ##
config = LoraConfig(task_type = "SEQ_2_SEQ_LM",
                    r = 8,
                    lora_alpha = 32,
                    target_modules = ["q", "v"])

model = AutoModelForSeq2SeqLM.from_pretrained("t5-base")
lora_model = LoraModel(model, config, "default")
