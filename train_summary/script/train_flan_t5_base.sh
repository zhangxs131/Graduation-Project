export CUDA_VISIBLE_DEVICES=6

python code/run_summarization.py \
    --model_name_or_path ../../../pretrain_model/pegasus_t5_summary \
    --do_train \
    --do_eval \
    --num_train_epochs 6.0 \
    --train_file data/train_1.json \
    --validation_file data/dev_1.json \
    --text_column 中文原文 \
    --summary_column 整编内容 \
    --source_prefix "summarize: " \
    --output_dir output/pegasus-t5-summary \
    --evaluation_strategy "steps" \
    --eval_steps 300 \
    --per_device_train_batch_size=4 \
    --per_device_eval_batch_size=4 \
    --save_total_limit 3 \
    --overwrite_output_dir \
    --metric_for_best_model rouge1 \
    --generation_max_length 512 \
    --predict_with_generate
