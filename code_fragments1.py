from transformers import AutoTokenizer


## ------------------------------------------------------ ##
dataset = load_dataset('openai/gsm8k', 'main')
train = dataset['train']
test = dataset['test']

## ------------------------------------------------------ ##
input_ids = tokenizer(text)

## ------------------------------------------------------ ##
output_text = tokenizer.decode(output_ids)

## ------------------------------------------------------ ##
model.generate(**ids)

## ------------------------------------------------------ ##
model.generate(**ids, do_sample = True)

## ------------------------------------------------------ ##
model.generate(**ids, do_sample = True, temperature = 0.7)

## ------------------------------------------------------ ##
model.generate(**ids, num_beams = 2)

## ------------------------------------------------------ ##
model.generate(**ids, num_beams = 3)

## ------------------------------------------------------ ##
AutoTokenizer.from_pretrained(model_name)(prompt_batch, padding = True)['input_ids']

## ------------------------------------------------------ ##
tokenizer = AutoTokenizer.from_pretrained(model_name)

## ------------------------------------------------------ ##
prompt = 'Using Huggingface is pretty manageable '

AutoTokenizer.from_pretrained('bert-base-uncased').tokenize(prompt)

## ------------------------------------------------------ ##
prompt = 'Using Huggingface is pretty manageable '

AutoTokenizer.from_pretrained('t5-small').tokenize(prompt)

## ------------------------------------------------------ ##
prompt = 'Using Huggingface is pretty manageable '

AutoTokenizer.from_pretrained('DeepSeek-ai/DeepSeek-math-7b-base').tokenize(prompt)
