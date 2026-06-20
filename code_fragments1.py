step_indicators = [r'step \d+', r'first', r'second', r'third', r'next', r'then', r'finally',
                r'calculate', r'find', r'determine', r'multiply', r'divide', r'add', r'subtract']

step_count = sum(len(re.findall(indicator, model_output)) for indicator in step_indicators)

if step_count >= 5:
    score += 0.4

elif step_count >= 3:
    score += 0.3

elif step_count >= 1:
    score += 0.2

## ------------------------------------------------------ ##
explanation_phrases = ['because', 'since', 'so', 'therefore', 'this means', 'we need to']

explanation_count = sum(1 for phrase in explanation_phrases if phrase in solution_lower)

if explanation_count >= 3:
    score += 0.3

elif explanation_count >= 1:
    score += 0.2
