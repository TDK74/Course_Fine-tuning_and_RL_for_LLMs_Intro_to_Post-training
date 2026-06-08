training_args = TrainingArguments(learning_rate = 2e-6,
                                weight_decay = 0.01,
                                per_device_train_batch_size = 20,
                                per_device_eval_batch_size = 20,
                                num_train_epochs = 3, )
## ------------------------------------------------------ ##
random.seed(seed)
np.random.seed(seed)
torch.manual_seed(seed)
