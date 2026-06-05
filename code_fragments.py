def get_function_names(path):
    with open(path, 'r') as f:
        lines = f.readlines()

    function_names = []

    for line in lines:
        if line.startswith('def'):
            function_names.append(line.split('(')[0].split(' ')[1])

    return function_names

## ------------------------------------------------------ ##
BASE_MODEL = "deepseek-ai/deepseek-math-7b-base"
FINETUNED_MODEL = "deepseek-ai/deepseek-math-7b-instruct"
RL_MODEL = "deepseek-ai/deepseek-math-7b-rl"

EXAMPLE_PROMPT = """Find the smallest positive integer N such that: N leaves remainder 1 when \
                    divided by 2, remainder 2 when divided by 3, remainder 3 when divided by 4, \
                    and so on, up to remainder 9 when divided by 10. N is divisible by 11"""

## ------------------------------------------------------ ##
gsm8k_dataset = load_dataset("gsm8k", "main")
