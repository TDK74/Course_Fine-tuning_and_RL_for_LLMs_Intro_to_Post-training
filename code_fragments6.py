GRPO_config = GRPOConfig(num_generations = 12, temperature = 0.7)

## ------------------------------------------------------ ##
mean_reward = sum(group_rewards) / len(group_rewards)
normalized_rewards = [r - mean_reward for r in group_rewards]

## ------------------------------------------------------ ##
def compute_rewards(prompts, completions):
    for i, unique_prompt in enumerate(unique_prompts):
        prompt_indices = [idx for idx, p in enumerate(prompts) if p == prompt]
        group_completions = [outputs[idx] for idx in prompt_indices]

        for j, out in enumerate(group_outputs):
            reward = reward_model.compute_reward(out, correct_out, prompt)
            group_rewards.append(reward)

    mean_reward = sum(group_rewards) / len(group_rewards)
    normalized_rewards = [r - mean_reward for r in group_rewards]

## ------------------------------------------------------ ##
trainer = GRPOTrainer(model = model, reward_funcs = compute_rewards, args = GRPO_config,
                    train_dataset = train_dataset, eval_dataset = eval_dataset,
                    processing_class = tokenizer, )

trainer.train()
