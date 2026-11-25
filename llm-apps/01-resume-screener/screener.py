from pathlib import Path
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).parent
INPUT_DIR = BASE_DIR / "inputs"

jd = (INPUT_DIR / "jd.txt").read_text(encoding="utf-8")
resume = (INPUT_DIR / "resume.txt").read_text(encoding="utf-8")

client = Anthropic()
messages = [{"role": "user", "content": "<resume>" + resume + "</resume>\n <job_description>" + jd + "</job_description>\n Review submitted resume for the provided job description."}]

response = client.messages.create(model="claude-sonnet-5-5", 
                       max_tokens=4096,
                       system="You are a helpful assistant helping to screen resumes. You check the fit of a resume against job description and provide a fit score in the range 1 to 10 with reasoning.",
                       messages=messages)

reply = "".join(b.text for b in response.content if b.type == "text")
print(reply)
