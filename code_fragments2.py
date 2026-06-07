## ------------------------------------------------------ ##
trainer = SFTTrainer(model = model_name, args = training_args, train_dataset = train_dataset,
                    eval_dataset = eval_dataset, )

## ------------------------------------------------------ ##
training_args = SFTConfig(completion_only_loss = True, ...)

trainer = SFTTrainer(model = model_name, args = training_args, train_dataset = train_dataset,
                    eval_dataset = eval_dataset, )

trainer.train()

## ------------------------------------------------------ ##
for epoch in range(num_epochs):
    for batch in train_dataloader:
        outputs = model(**batch)
        loss = outputs.loss
        loss.backward()
        optimizer.step()
