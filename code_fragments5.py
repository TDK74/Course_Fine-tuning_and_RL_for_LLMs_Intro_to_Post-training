def math_reward(response, correct_answer):
    if (extract_final_answer(response) == correct_answer):
        return 1.0

    else:
        return 0.0

## ------------------------------------------------------ ##
def format_reward(response):
    if ("$" in response and "$" in response):
        return 1.0

    else:
        return 0.0

## ------------------------------------------------------ ##
def language_consistency_reward(response):
    if consistent_language(response):
        return 1.0

    else:
        return -0.5

## ------------------------------------------------------ ##
def combined_reward(response, correct_answer):
    accuracy = math_reward(response, correct_answer)
    format_check = format_reward(response)
    language_check = language_consistency_reward(response)

    return accuracy + format_check + language_check

## ------------------------------------------------------ ##
if predicted == correct_answer:
    reward = 1.0
else:
    relative_error = abs(predicted - correct_answer) / correct_answer

if relative_error < 0.01:
    reward = 1.0
elif relative_error < 0.1:
    reward = 0.8
elif relative_error < 0.3:
    reward = 0.5
