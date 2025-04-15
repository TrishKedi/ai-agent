from planner import plan_week
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

tokenizer = AutoTokenizer.from_pretrained('tiiuae/falcon-rw-1b')
model = AutoModelForCausalLM.from_pretrained('tiiuae/falcon-rw-1b')
pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=512)

prompt = "Plan my week including gym, study, and freelance schedule"
response = pipe(prompt)

result = pipe(prompt, do_sample=True, temperature=0.7)
print(result[0]['generated_text'].strip())