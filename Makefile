PYTHON_INTERPRETER=python3

help:
	@echo "Use \`make <target>\` where \`<target>\` is one of"
	@echo "  init   initialize friends"

init:
	$(PYTHON_INTERPRETER) scripts/init_friends_ids.py > data/friends_ids.json
