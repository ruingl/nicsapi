from g4f.client import Client
from flask import (
  Flask,
  jsonify,
  request
)

app = Flask(__name__)

@app.route('/api/gpt', methods=['POST'])
def gpt():
  d = request.get_json()
  m = d.get('messages')

  c = Client()
  r = c.chat.completions.create(
    model='gpt-4o-mini',
    messages=m,
    web_search=False
  )

  return jsonify({
    'role': 'assistant',
    'content': r.choices[0].message.content
  })

if __name__ == "__main__":
  app.run(port=3000, debug=True)
